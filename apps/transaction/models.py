import uuid

from django.utils import timezone
from django.db import models

from apps.company.models import Company
from apps.user.models import BaseModel

TRANSACTION_STATUS_CHOICES = [
    ('closed', 'Closed'),
    ('reversed', 'Reversed'),
    ('pending', 'Pending'),
]


# Create your models here.
class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_id = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, related_name='transactions')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    status_transaction = models.CharField(
        max_length=20,
        choices=TRANSACTION_STATUS_CHOICES,
        default='pending',)
    status_approved = models.BooleanField(default=False)
    final_payment = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id'], name='unique_transaction_id')
        ]

    def __str__(self):
        return str(self.id)
    
    @property
    def set_real_price(self):
        if self.status_transaction != 'reversed':
            base_price = ServicePriceCatalog.objects.get(company_id=self.company_id).base_price
            if base_price:
                gross_price = self.price - base_price
                real_price = self.price - gross_price
                self.price = real_price
                self.save()
    

class TransactionStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class ServicePriceCatalog(BaseModel, models.Model):
    company_id = models.OneToOneField(Company, on_delete=models.PROTECT, null=True, related_name='service_price_catalogs')
    base_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return str(self.id)
