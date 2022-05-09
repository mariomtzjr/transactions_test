from dataclasses import fields
from django.contrib import admin

from .models import CountryCode, Address


# Register your models here.
@admin.register(CountryCode)
class CountryCodeAdmin(admin.ModelAdmin):
    fields = ('id', 'country_code', 'country_name')
    list_display = ('id', 'country_code', 'country_name')
    readonly_fields = ('id', 'country_code', 'country_name')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    fields = ('id', 'company_id', 'street', 'number', 'colony', 'city', 'state', 'country_code_id', 'zip_code',)
    list_display = ('id', 'company_id', 'country_code_id',)
    readonly_fields = ('id', 'company_id', 'street', 'number', 'colony', 'city', 'state', 'country_code_id', 'zip_code')