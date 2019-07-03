from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Coach)
class coachAdmin(admin.ModelAdmin):
    list_display = ('id', 'coach_id', 'coach_name','coach_phone', 'coach_email', 'coach_age', 'coach_seniority','coach_ismaster')
    list_filter = ('coach_id', 'coach_name',)
    search_fields = ('coach_name',)
    list_display_links = ('id', 'coach_id', 'coach_name')
    # list_editable = ('top', 'category')