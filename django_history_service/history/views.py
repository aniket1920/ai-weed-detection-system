from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DetectionRecord
from .serializers import DetectionRecordSerializer
from django.utils import timezone
from datetime import timedelta
from django.db.models import Avg, Max, Min, Count, Sum


class DetectionReportView(APIView):
    """
    GET /api/report/          → full report for last 7 days
    GET /api/report/?days=30  → last 30 days
    GET /api/report/?days=1   → today only
    """

    def get(self, request):
        days = int(request.query_params.get('days', 7))
        since = timezone.now() - timedelta(days=days)

        records = DetectionRecord.objects.filter(detected_at__gte=since)

        if not records.exists():
            return Response({
                'period_days': days,
                'message': f'No detections in the last {days} day(s).'
            })

        # --- Aggregate stats ---
        stats = records.aggregate(
            total_scans=Count('id'),
            total_weeds_found=Sum('weed_count'),
            avg_weeds=Avg('weed_count'),
            max_weeds=Max('weed_count'),
            min_weeds=Min('weed_count'),
        )

        # --- Daily breakdown ---
        daily_data = {}
        for record in records:
            day = record.detected_at.strftime('%Y-%m-%d')
            if day not in daily_data:
                daily_data[day] = {'scans': 0, 'total_weeds': 0}
            daily_data[day]['scans'] += 1
            daily_data[day]['total_weeds'] += record.weed_count

        daily_breakdown = [
            {'date': day, **values}
            for day, values in sorted(daily_data.items())
        ]

        # --- Alerts: images with weed_count above average ---
        avg = stats['avg_weeds'] or 0
        alerts = records.filter(weed_count__gt=avg).values(
            'id', 'image_name', 'weed_count', 'detected_at'
        )

        return Response({
            'period_days': days,
            'summary': {
                'total_scans': stats['total_scans'],
                'total_weeds_found': stats['total_weeds_found'],
                'average_weeds_per_scan': round(avg, 2),
                'max_weeds_in_single_scan': stats['max_weeds'],
                'min_weeds_in_single_scan': stats['min_weeds'],
            },
            'daily_breakdown': daily_breakdown,
            'alerts': {
                'description': 'Images with weed count above average — needs attention',
                'count': alerts.count(),
                'records': list(alerts),
            }
        })


class DetectionRecordListCreateView(APIView):
    """
    GET  /api/history/        → list all records (supports ?min_weeds=N filter)
    POST /api/history/        → save a new detection result
    """

    def get(self, request):
        records = DetectionRecord.objects.all()

        # Optional filter: ?min_weeds=3
        min_weeds = request.query_params.get('min_weeds')
        if min_weeds is not None:
            records = records.filter(weed_count__gte=min_weeds)

        serializer = DetectionRecordSerializer(records, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DetectionRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetectionRecordDetailView(APIView):
    """
    GET    /api/history/<id>/  → single record
    DELETE /api/history/<id>/  → delete a record
    """

    def get_object(self, pk):
        try:
            return DetectionRecord.objects.get(pk=pk)
        except DetectionRecord.DoesNotExist:
            return None

    def get(self, request, pk):
        record = self.get_object(pk)
        if record is None:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = DetectionRecordSerializer(record)
        return Response(serializer.data)

    def delete(self, request, pk):
        record = self.get_object(pk)
        if record is None:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DetectionStatsView(APIView):
    """
    GET /api/history/stats/  → summary stats (this is the "fancy" part)
    """

    def get(self, request):
        records = DetectionRecord.objects.all()
        total = records.count()

        if total == 0:
            return Response({'message': 'No detection records yet.'})

        weed_counts = list(records.values_list('weed_count', flat=True))
        avg_weeds = sum(weed_counts) / total
        max_weeds = max(weed_counts)
        min_weeds = min(weed_counts)

        return Response({
            'total_detections': total,
            'average_weeds_per_image': round(avg_weeds, 2),
            'max_weeds_detected': max_weeds,
            'min_weeds_detected': min_weeds,
        })