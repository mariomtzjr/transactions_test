from django.contrib import admin

from .models import Transaction, ServicePriceCatalog


# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    fields = ('id', 'company_id', 'price', 'date', 'status_transaction', 'status_approved', 'final_payment', 'created_at', 'updated_at')
    list_display = ('id', 'company_id', 'price', 'status_transaction', 'status_approved', 'final_payment',)
    readonly_fields = ('id', 'company_id', 'price', 'date', 'status_transaction', 'status_approved', 'final_payment', 'created_at', 'updated_at')
    search_fields = ('id', 'company_id__id', 'company_id__name')
    list_filter = ('status_transaction', 'status_approved', 'final_payment',)


@admin.register(ServicePriceCatalog)
class ServicePriceCatalogAdmin(admin.ModelAdmin):
    fields = ('id', 'company_id', 'base_price',)
    list_display = ('id', 'company_id', 'base_price',)
    readonly_fields = ('id', 'company_id',)
    search_fields = ('company_id__name',)
