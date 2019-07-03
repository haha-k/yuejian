from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Activity)
class activityAdmin(admin.ModelAdmin):
    list_display = ('id', 'activityId', 'activityName','activityDesc','activityPrice', 'hits', 'fans', 'image', 'createDate')
    list_filter = ('createDate', 'activityName',)
    search_fields = ('activityName',)
    list_display_links = ('id', 'activityId', 'activityName')
    # list_editable = ('top', 'category')
    list_per_page = 10

@admin.register(Apply)
class ApplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId','userName','aotId', 'aotName','activityOrTrain','createDate')
    list_filter = ('createDate', 'aotName','userName')
    search_fields = ('aotName','userName')
    list_display_links = ('id','userId','userName','aotId', 'aotName')
    # list_editable = ('top', 'category')
    list_per_page = 10