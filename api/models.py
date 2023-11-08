from django.db import models
import shortuuid


class Link(models.Model):
    original_url = models.URLField(max_length=500)
    short_url = models.CharField(max_length=40, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_url, self.short_url

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = shortuuid.uuid()[:8]
        super().save(*args, **kwargs)

