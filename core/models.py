from django.db import models

# Create your models here.

class Config(models.Model):
    key = models.CharField(max_length=120)
    value = models.CharField(max_length=120)

    def __str__(self):
        return self.key