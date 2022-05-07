import uuid

from django.utils import timezone
from django.db import models

from apps.company.models import Company

TRANSACTION_STATUS_CHOICES = [
    ('closed', 'Closed'),
    ('reversed', 'Reversed'),
    ('pending', 'Pending'),
]


# Create your models here.
class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_id = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    status_transaction = models.CharField(
        max_length=20,
        choices=TRANSACTION_STATUS_CHOICES,
        default='pending',)
    status_approved = models.BooleanField(default=False)
    final_payment = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_id.name
    
    def get_final_payment(self):
        if self.status_transaction == 'closed' and self.status_approved == True:
            self.final_payment = True
        return self.final_payment



class TransactionStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)