from django.contrib import admin
from .models import Contest


# Register your models here.
@admin.register(Contest)
class contestAdmin(admin.ModelAdmin):
    list_display = ('id', 'contest_id', 'contest_name','contest_desc', 'contest_pic','contest_date','create_date')
    list_filter = ('create_date', 'contest_name',)
    search_fields = ('contest_name',)
    list_display_links = ('id', 'contest_id', 'contest_name')
    # list_editable = ('top', 'category')
    list_per_page = 10