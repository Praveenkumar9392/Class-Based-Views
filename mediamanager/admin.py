from django.contrib import admin

# Register your models here.
from .models import MediaItem,MediaFolder

admin.site.register(MediaItem)
admin.site.register(MediaFolder)