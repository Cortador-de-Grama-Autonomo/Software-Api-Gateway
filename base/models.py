from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.reverse_related import OneToOneRel

# Create your models here.
class GrassMachine(models.Model):
    name = models.CharField(max_length=25, default='')
    serie_number = models.CharField(max_length=25, null=True)
    battery_percentage = models.IntegerField(null=True)
    model = models.CharField(max_length=10, null=True)
    power = models.IntegerField(null=True)
    voltage = models.IntegerField(null=True)
    motor_type = models.CharField(max_length=20, null=True)
    cut_type = models.CharField(max_length=20, null=True)
    rotation_number = models.IntegerField(null=True)
    qr_code_identifier = models.CharField(max_length=20, unique=True, default='')
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


    def __str__(self) -> str:
        return self.model + self.qr_code_identifier
