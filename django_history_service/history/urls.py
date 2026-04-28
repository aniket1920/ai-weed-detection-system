from django.urls import path
from .views import (
    DetectionRecordListCreateView,
    DetectionRecordDetailView,
    DetectionStatsView,
    DetectionReportView,
)

urlpatterns = [
    path('history/', DetectionRecordListCreateView.as_view(), name='history-list-create'),
    path('history/<int:pk>/', DetectionRecordDetailView.as_view(), name='history-detail'),
    path('history/stats/', DetectionStatsView.as_view(), name='history-stats'),
    path('report/', DetectionReportView.as_view(), name='detection-report'),
]