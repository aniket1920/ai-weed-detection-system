from django.contrib import admin
from .models import DetectionRecord

@admin.register(DetectionRecord)
class DetectionRecordAdmin(admin.ModelAdmin):
    list_display = ('image_name', 'weed_count', 'confidence_threshold', 'processing_time', 'detected_at')
    list_filter = ('detected_at',)
    search_fields = ('image_name',)