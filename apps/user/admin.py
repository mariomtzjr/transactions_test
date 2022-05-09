from django.contrib import admin

from .models import CompanyUser, UserType, UserContactType


# Register your models here.
@admin.register(CompanyUser)
class CompanyUserAdmin(admin.ModelAdmin):
    pass

@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(UserContactType)
class UserContactTypeAdmin(admin.ModelAdmin):
    pass