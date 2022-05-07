import uuid
from datetime import datetime

from django.db import models


TRANSACTION_STATUS_CHOICES = [
    ('closed', 'Closed'),
    ('reversed', 'Reversed'),
    ('pending', 'Pending'),
]


# Create your models here.
class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_id = models.ForeignKey('apps.Company', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=datetime.now())
    status = models.CharField(
        max_length=20,
        choices=TRANSACTION_STATUS_CHOICES,
        default='pending',)
    aprove = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_id.name


class TransactionStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)