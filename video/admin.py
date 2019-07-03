from django.contrib import admin
from .models import Video

# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'video_id', 'video_name','video_type', 'video_pic', 'club_id')
    list_filter = ('video_name',)
    search_fields = ('video_name',)
    list_display_links = ('id', 'video_id', 'video_name')
    # list_editable = ('top', 'category')