from django.contrib import admin

from .models import Account, AccountType


# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    pass
