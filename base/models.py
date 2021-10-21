from django.db import models

# Create your models here.
class GrassMachine(models.Model):
    model = models.CharField(max_length=10, null=True)
    qr_code_identifier = models.CharField(max_length=20, unique=True, default='')
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return super().__str__()
