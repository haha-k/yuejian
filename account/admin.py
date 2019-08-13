from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(Account)
class accountAdmin(admin.ModelAdmin):
    list_display = ('id', 'username','telephone', 'nickname', 'gender', 'birthdate', 'avator_url','register_time')
    list_filter = ('nickname', 'username','telephone',)
    search_fields = ('nickname', 'username','register_time')
    list_display_links = ('id', 'username','nickname')
    # list_editable = ('top', 'category')
    list_per_page = 20
