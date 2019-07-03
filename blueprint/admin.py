from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Blueprint)
class BlueprintAdmin(admin.ModelAdmin):
    list_display = ('id','blueprint_id', 'blueprint_content', 'blueprint_picture','create_time', 'club_id')
    list_filter = ('blueprint_id', )
    search_fields = ('blueprint_id',)
    list_display_links = ('id', 'blueprint_id')
    # list_editable = ('top', 'category')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','comment_id', 'comment_content', 'comment_time', 'comment_user_id','blueprint_id')
    list_filter = ('comment_id', )
    search_fields = ('comment_id',)
    list_display_links = ('id', 'comment_id')

@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ('id','picture_id', 'picture_address', 'create_time')
    list_filter = ('picture_id', )
    search_fields = ('picture_id',)
    list_display_links = ('id', 'picture_id')