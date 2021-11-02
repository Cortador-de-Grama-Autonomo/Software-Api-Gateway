from django.db import models

# Create your models here.
class Locations(models.Model):
    name = models.TextField()
    description = models.TextField(null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self) -> str:
        return self.name
