from django.db import models
from django.conf import settings

# Create your models here.


class Post (models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title           = models.CharField(max_length=120)
    # slug = models.SlugField(unique=True)
    # image = models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field    = models.IntegerField(default=0)
    width_field     = models.IntegerField(default=0)
    content         = models.TextField()
    is_done         = models.BooleanField(default=False)
    draft           = models.BooleanField(default=False)
    # publish = models.DateField(auto_now=False, auto_now_add=False)
    update          = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp       = models.DateTimeField(auto_now=False, auto_now_add=True)
    read_time       = models.TimeField(null=True, blank=True)
    is_doing        = models.BooleanField(default=False)
    assignee_id     = models.CharField(max_length=120, blank=True)
    progress_percent= models.IntegerField(default=0)
    default_cost    = models.FloatField(null=True)
    actual_cost     = models.FloatField(null=True)

    def __str__(self):
        return self.title
