from django.contrib import admin

from .models import Document, Affair, CategoryAffair, CategoryDocument

# Register your models here.
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'document_name', 'document_date', 'document_type']
    search_fields = ['document_name', 'document_type']
    list_filter = ['document_date', 'document_type']
    ordering = ['document_date']
    list_per_page = 20

@admin.register(Affair)
class AffairAdmin(admin.ModelAdmin):    
    list_display = ['id', 'affair_name', 'affair_date', 'affair_status']
    search_fields = ['affair_name']
    list_filter = ['affair_date', 'affair_status']
    ordering = ['affair_date']
    list_per_page = 20

@admin.register(CategoryAffair)
class CategoryAffairAdmin(admin.ModelAdmin):
    list_display = ['id', 'affair_id', 'cat_aff_name']
    search_fields = ['cat_aff_name']
    ordering = ['cat_aff_name']
    list_per_page = 20

@admin.register(CategoryDocument)
class CategoryDocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'document_id', 'cat_doc_name']
    search_fields = ['cat_doc_name']
    ordering = ['cat_doc_name']
    list_per_page = 20