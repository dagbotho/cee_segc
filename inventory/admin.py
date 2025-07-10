from django.contrib import admin

from .models import ConstructionSite, Transfer, Stock, WarehouseCategory, Warehouse, Delivery, DeliveryDetail, Location

# Register your models here.
@admin.register(ConstructionSite)
class ConstructionSiteAdmin(admin.ModelAdmin):
    list_display = ['id', 'site_name', 'site_address', 'site_phone_number', 'site_email', 'site_country', 'site_city', 'site_postal_code']
    search_fields = ['site_name', 'site_address', 'site_email']
    list_filter = ['site_country', 'site_city']
    ordering = ['site_name']
    list_per_page = 20


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ['id', 'transfer_date', 'transfer_quantity', 'transfer_from', 'transfer_to', 'transfer_description', 'transfer_received_date']
    search_fields = ['transfer_from__site_name', 'transfer_to__site_name']
    list_filter = ['transfer_date', 'transfer_from__site_name', 'transfer_to__site_name']
    ordering = ['transfer_date']
    list_per_page = 20


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'quantity_available', 'minimum_stock_level', 'maximum_stock_level', 'reorder_point']
    search_fields = ['product_name']
    list_filter = ['quantity_available', 'minimum_stock_level', 'maximum_stock_level']
    ordering = ['product_name']
    list_per_page = 20


@admin.register(WarehouseCategory)
class WarehouseCategoryAdmin(admin.ModelAdmin): 
    list_display = ['id', 'category_name']
    search_fields = ['category_name']
    ordering = ['category_name']
    list_per_page = 20


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin): 
    list_display = ['id', 'warehouse_name', 'warehouse_address', 'warehouse_phone_number', 'warehouse_email', 'warehouse_country', 'warehouse_city', 'warehouse_postal_code', 'isRefrigerated']
    search_fields = ['warehouse_name', 'warehouse_address', 'warehouse_email']
    list_filter = ['warehouse_country', 'warehouse_city', 'isRefrigerated']
    ordering = ['warehouse_name']
    list_per_page = 20


@admin.register(Delivery)
class DeleveryAdmin(admin.ModelAdmin):
    list_display = ['id', 'sales_date']
    search_fields = ['delivery_from__site_name', 'delivery_to__site_name']
    list_filter = ['delivery_date', 'delivery_from__site_name', 'delivery_to__site_name']
    ordering = ['sales_date']
    list_per_page = 20


@admin.register(DeliveryDetail)
class DeliveryItemAdmin(admin.ModelAdmin):  
    list_display = ['id', 'delivery', 'product', 'quantity']
    search_fields = ['delivery__delivery_from__site_name', 'product__name']
    list_filter = ['delivery__delivery_date', 'product__name']
    ordering = ['delivery__delivery_date']
    list_per_page = 20


@admin.register(Location)  
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'location_name', 'location_address', 'location_phone_number', 'location_email', 'location_country', 'location_city', 'location_postal_code']
    search_fields = ['location_name', 'location_address', 'location_email']
    list_filter = ['location_country', 'location_city']
    ordering = ['location_name']
    list_per_page = 20