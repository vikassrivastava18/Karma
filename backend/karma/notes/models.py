from django.db import models
from django.contrib.postgres.fields import JSONField


# If using sqlite and Django < 4.2, import JSONField from django.db.models
try:
    from django.db.models import JSONField as BuiltinJSONField
except Exception:
    from django.contrib.postgres.fields import JSONField as BuiltinJSONField


class Note(models.Model):
    title = models.CharField(max_length=255)
    blocks = BuiltinJSONField(default=list) # list of blocks: {type: 'heading'|'paragraph'|'image', content: '...'}
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Simple image model so we can store uploaded files and return a URL
class UploadedImage(models.Model):
    file = models.ImageField(upload_to='note_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.file.name)