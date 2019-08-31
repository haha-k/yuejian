from django.contrib import admin
from .models import *

# Register your models here.

# @admin.register(Blueprint)
# class BlueprintAdmin(admin.ModelAdmin):
#     list_display = ('blueprint_id', 'blueprint_content', 'blueprint_picture','create_date', 'user_id')
#     list_filter = ('blueprint_id', )
#     search_fields = ('blueprint_id',)
#     list_display_links = ( 'blueprint_id',)
#     # list_editable = ('top', 'category')

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('comment_id', 'comment_content', 'comment_time', 'from_user_id','blueprint_id')
#     list_filter = ('comment_id', )
#     search_fields = ('comment_id',)
#     list_display_links = ('comment_id',)

# @admin.register(Picture)
# class PictureAdmin(admin.ModelAdmin):
#     list_display = ('picture_id', 'picture_address', 'create_time')
#     list_filter = ('picture_id', )
#     search_fields = ('picture_id',)
#     list_display_links = ('picture_id',)