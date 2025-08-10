

# Register your models here.
from django.contrib import admin
from .models import URL

@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ('short_code', 'original_url', 'clicks', 'created_at')
    search_fields = ('original_url', 'short_code')
    readonly_fields = ('clicks', 'created_at')