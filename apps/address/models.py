import uuid

from django.db import models

from apps.user.models import BaseModel
from apps.company.models import Company

# Create your models here.
class CountryCode(BaseModel, models.Model):
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=50)

    def __str__(self):
        return self.country_name

    def set_pk(self):
        self.pk = uuid.uuid4()


class Address(BaseModel, models.Model):
    company_id = models.OneToOneField(Company, on_delete=models.SET_NULL, null=True)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    colony = models.CharField(max_length=100, default=None, null=True, blank=True)
    city = models.CharField(max_length=100, default=None, null=True, blank=True)
    state = models.CharField(max_length=100, default=None, null=True, blank=True)
    country_code_id = models.OneToOneField(CountryCode, on_delete=models.SET_NULL, null=True)
    zip_code = models.CharField(max_length=10, default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id}"