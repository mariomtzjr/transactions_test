from django.contrib import admin

from .models import Account, AccountType


# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'clabe', 'account_number', 'company_id', 'account_type')
    readonly_fields = ('id', 'clabe', 'account_number', 'company_id', 'account_type')


@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')
    readonly_fields = ('id', 'type_name')
