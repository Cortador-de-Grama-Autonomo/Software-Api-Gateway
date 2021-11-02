from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.reverse_related import OneToOneRel

# Create your models here.
class GrassMachine(models.Model):
    model = models.CharField(max_length=10, null=True)
    qr_code_identifier = models.CharField(max_length=20, unique=True, default='')
    description = models.TextField(null=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.model + self.qr_code_identifier
