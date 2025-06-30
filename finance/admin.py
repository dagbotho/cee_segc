from django.contrib import admin

from .models import JournalDefinition, Invoice, PaymentRecord, ThirdParty, CategoryThirdParty

# Register your models here.
@admin.register(JournalDefinition)
class JournalDefinitionAdmin(admin.ModelAdmin):
    list_display = ['id', 'journal_name']
    search_fields = ['journal_name']
    ordering = ['journal_name']
    list_per_page = 20

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'invoice_number', 'invoice_date', 'invoice_amount']
    search_fields = ['invoice_number']
    list_filter = ['invoice_date']
    ordering = ['invoice_date']
    list_per_page = 20

@admin.register(PaymentRecord)
class PaymentRecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'invoice_id']
    search_fields = ['invoice_id__invoice_number']
    list_filter = ['invoice_id__invoice_date']
    ordering = ['invoice_id__invoice_date']
    list_per_page = 20

@admin.register(ThirdParty)
class ThirdPartyAdmin(admin.ModelAdmin):    
    list_display = ['id', 'third_party_name', 'third_party_address', 'third_party_phone_number', 'third_party_email', 'third_party_country', 'third_party_city', 'third_party_postal_code']
    search_fields = ['third_party_name', 'third_party_address', 'third_party_email']
    list_filter = ['third_party_country', 'third_party_city']
    ordering = ['third_party_name']
    list_per_page = 20

@admin.register(CategoryThirdParty)
class CategoryThirdPartyAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']
    search_fields = ['category_name']
    ordering = ['category_name']
    list_per_page = 20