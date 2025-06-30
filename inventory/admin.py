from django.contrib import admin

from .models import ConstructionSite

# Register your models here.
@admin.register(ConstructionSite)
class ConstructionSiteAdmin(admin.ModelAdmin):
    list_display = ['id', 'site_name', 'site_address', 'site_phone_number', 'site_email', 'site_country', 'site_city', 'site_postal_code']
    search_fields = ['site_name', 'site_address', 'site_email']
    list_filter = ['site_country', 'site_city']
    ordering = ['site_name']
    list_per_page = 20