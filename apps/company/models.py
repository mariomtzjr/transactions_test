import uuid

from django.db import models


COMPANY_STATUS_CHOICES = [
    ('active', 'Active'),
    ('inactive', 'Inactive'),
]


# Create your models here.
class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, unique=True)
    company_rfc = models.CharField(max_length=20, unique=True, null=True, blank=True)
    company_phone = models.CharField(max_length=20, null=True, blank=True)
    company_email = models.EmailField(max_length=100, null=True, blank=True)
    company_estatus = models.CharField(
        max_length=20,
        choices=COMPANY_STATUS_CHOICES,
        default='active',)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id'], name='unique_company_id')
        ]

    def __str__(self):
        return self.name