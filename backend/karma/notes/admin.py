from django.contrib import admin

from .models import Note, NoteTopic
# Register your models here.

admin.site.register(Note)
admin.site.register(NoteTopic)