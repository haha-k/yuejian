from django.contrib import admin
from .models import Contest


# Register your models here.
@admin.register(Contest)
class contestAdmin(admin.ModelAdmin):
    list_display = ('contest_id', 'contest_title','contest_desc', 'contest_pic','contest_date','create_date')
    list_filter = ('create_date', 'contest_title',)
    search_fields = ('contest_title',)
    list_display_links = ('contest_id', 'contest_title')
    # list_editable = ('top', 'category')
    list_per_page = 10