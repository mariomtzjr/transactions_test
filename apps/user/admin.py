from django.contrib import admin

from .models import CompanyUser, UserType, UserContactType


# Register your models here.
@admin.register(CompanyUser)
class CompanyUserAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'lastname', 'company_id', 'user_type_id', 'contact_type_id', 'created_at', 'updated_at')
    list_display = ('id', 'name', 'lastname', 'company_id', 'user_type_id', 'contact_type_id',)
    readonly_fields = ('id', 'name', 'lastname', 'company_id', 'user_type_id', 'contact_type_id', 'created_at', 'updated_at')


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    fields = ('id', 'type_name',)
    list_display = ('id', 'type_name',)
    readonly_fields = ('id', 'type_name',)


@admin.register(UserContactType)
class UserContactTypeAdmin(admin.ModelAdmin):
    fields = ('id', 'contact_type_name', 'contact_type_value',)
    list_display = ('id', 'contact_type_name', 'contact_type_value',)
    readonly_fields = ('id', 'contact_type_name', 'contact_type_value',)