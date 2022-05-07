import uuid

from django.db import models


COMPANY_STATUS_CHOICES = [
    ('active', 'Active'),
    ('inactive', 'Inactive'),
]


# Create your models here.
class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    company_estatus = models.CharField(
        max_length=20,
        choices=COMPANY_STATUS_CHOICES,
        default='active',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name