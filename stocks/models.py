from django.db import models

# Create your models here.


class Stock(models.Model):
    symbol = models.CharField(max_length=120)
    price_data = models.TextField(null=True)
    financial_data = models.TextField(null=True)
    close = models.FloatField(null=True)
    ROE = models.FloatField(null=True)
    EPS = models.FloatField(null=True)
    volume = models.FloatField(null=True)
    RSI_14 = models.FloatField(null=True)
    RSI_14_diff = models.FloatField(null=True)
    market_capitalization = models.FloatField(null=True)

    def __str__(self):
        return self.symbol
