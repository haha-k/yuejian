from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Activity)
class activityAdmin(admin.ModelAdmin):
    list_display = ('activity_id', 'activity_title','activity_desc','activity_price','create_date','update_date')
    list_filter = ('create_date', 'activity_title',)
    search_fields = ('activity_name',)
    list_display_links = ('activity_id', 'activity_title')
    # list_editable = ('top', 'category')
    list_per_page = 10

@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    list_display = ('apply_id', 'user_id','user_id','activity_id', 'train_id','create_date','update_date')
    list_filter = ('create_date','user_id')
    search_fields = ('user_id',)
    list_display_links = ('user_id','activity_id', 'train_id')
    # list_editable = ('top', 'category')
    list_per_page = 10