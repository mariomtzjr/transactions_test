from django.contrib import admin

from .models import Company


# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'company_rfc', 'company_phone', 'company_email', 'company_status', 'created_at', 'updated_at')
    list_display = ('id', 'name', 'company_estatus')
    readonly_fields = fields = ('id', 'name', 'company_estatus', 'created_at', 'updated_at')
