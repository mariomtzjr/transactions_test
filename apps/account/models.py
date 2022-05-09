import uuid

from django.db import models

from apps.company.models import Company
from apps.user.models import BaseModel


# Create your models here.
class AccountType(BaseModel, models.Model):
    type_name = models.CharField(max_length=10)

    def __str__(self):
        return self.type_name
        
    def set_pk(self):
        self.pk = uuid.uuid4().hex[:8]


class Account(BaseModel, models.Model):
    clabe = models.CharField(max_length=50, default=None, null=True, blank=True)
    account_number = models.CharField(max_length=20, default=None, null=True, blank=True)
    company_id = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    account_type = models.OneToOneField(AccountType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.account_number
