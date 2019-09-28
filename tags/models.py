from django.db import models
from model_utils.models import SoftDeletableModel, TimeStampedModel
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Tag(TimeStampedModel, SoftDeletableModel):
    name = models.CharField(max_length=120, null=False, blank=False)

    def __str__(self):
        self.name
    
    class Meta:
        ordering = ('-created',)
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

