from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_id','course_title','course_intro', 'club_id', 'course_cover', 'course_site','course_type')
    list_filter = ('course_title', 'club_id',)
    search_fields = ('course_title',)
    list_display_links = ('course_id', 'course_title')
    # list_editable = ('top', 'category')