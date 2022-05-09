from django.contrib import admin

from .models import CountryCode, Address


# Register your models here.
@admin.register(CountryCode)
class CountryCodeAdmin(admin.ModelAdmin):
    pass

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass