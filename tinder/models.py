from django.db import models

# Create your models here.


class Tinder(models.Model):
    user_id = models.TextField(unique=True)
    content = models.TextField()
    status = models.CharField(default='active', max_length=100)

    def __str__(self):
        return self.user_id
