from django.db import models

# Create your models here.


class Stock(models.Model):
    symbol = models.CharField(max_length=120)
    price_data = models.TextField(null=True)
    financial_data = models.TextField(null=True)

    def __str__(self):
        return self.symbol
