from django.contrib import admin
from .models import Video

# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_id', 'video_title','video_type', 'video_pic', 'club_id')
    list_filter = ('video_title',)
    search_fields = ('video_title',)
    list_display_links = ('video_id', 'video_title')
    # list_editable = ('top', 'category')