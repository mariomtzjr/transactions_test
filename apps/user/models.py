import uuid

from django.db import models

from apps.company.models import Company

USER_CONTACT_TYPE_CHOICES = [
    ('email', 'Email'),
    ('phone', 'Phone'),
]


# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=None, editable=False)

    def set_pk(self):
        self.id = uuid.uuid4()

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.set_pk()
            super(BaseModel, self).save(*args, **kwargs)


class UserType(BaseModel, models.Model):
    type_name = models.CharField(max_length=50)

    def set_pk(self):
        self.id = uuid.uuid4()

    def __str__(self):
        return self.type_name


class UserContactType(BaseModel, models.Model):
    contact_type_name = models.CharField(max_length=10, choices=USER_CONTACT_TYPE_CHOICES, default=None, null=True, blank=True)
    contact_type_value = models.CharField(max_length=50, default=None, null=True, blank=True)

    def set_pk(self):
        self.id = uuid.uuid4()
    
    def __str__(self):
        return self.contact_type_value


class CompanyUser(BaseModel, models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    company_id = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    user_type_id = models.OneToOneField(UserType, on_delete=models.SET_NULL, null=True)
    contact_type_id = models.ForeignKey(UserContactType, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.lastname}"