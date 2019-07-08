from django.db import models

# Create your models here.

class Tinder(models.Model):
    user_id = models.TextField(unique=True)
    content = models.TextField()
    