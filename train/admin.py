from django.contrib import admin
from .models import Train

# Register your models here.

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('id', 'train_id', 'train_title','train_address', 'train_date', 'train_price', 'train_show','club_id')
    list_filter = ('train_title',)
    search_fields = ('train_title',)
    list_display_links = ('id', 'train_id', 'train_title')
    # list_editable = ('top', 'category')