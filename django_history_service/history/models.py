from django.db import models

class DetectionRecord(models.Model):
    image_name = models.CharField(max_length=255)
    weed_count = models.IntegerField()
    confidence_threshold = models.FloatField()
    processing_time = models.FloatField(help_text="Processing time in seconds")
    detected_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-detected_at']

    def __str__(self):
        return f"{self.image_name} — {self.weed_count} weeds at {self.detected_at:%Y-%m-%d %H:%M}"