from django.contrib import admin

from .models import Transaction


# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    fields = ('id', 'company_id', 'price', 'date', 'status_transaction', 'status_approved', 'final_payment', 'created_at', 'updated_at')
    list_display = ('id', 'company_id', 'status_transaction', 'status_approved', 'final_payment',)
    readonly_fields = ('id', 'company_id', 'price', 'date', 'status_transaction', 'status_approved', 'final_payment', 'created_at', 'updated_at')