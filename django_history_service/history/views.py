from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import DetectionRecord
from .serializers import DetectionRecordSerializer


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