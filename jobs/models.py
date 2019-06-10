from django.db import models

# Create your models here.


class Job(models.Model):
    # time = models.IntegerField(null=False, blank=False)
    searchWord = models.CharField(max_length=120, null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return 'Hello'
