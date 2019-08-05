from django.db import models
import datetime
# Create your models here.


class Stock(models.Model):
    Symbol = models.CharField(max_length=120)
    # price_data = models.TextField(null=True)
    financial_data = models.TextField(null=True)
    Close = models.FloatField(null=True)
    Open = models.FloatField(null=True)
    High = models.FloatField(null=True)
    Low = models.FloatField(null=True)
    Volume = models.FloatField(null=True)
    Value = models.FloatField(null=True)
    Date = models.CharField(null=True, max_length=120)
    yesterday_Close = models.FloatField(null=True)
    ROE = models.FloatField(null=True)
    EPS = models.FloatField(null=True)
    Volume = models.FloatField(null=True)
    RSI_14 = models.FloatField(null=True)
    RSI_14_diff = models.FloatField(null=True)
    MarketCapitalization = models.FloatField(null=True)
    today_capitalization = models.FloatField(null=True)
    percentage_change_in_price = models.FloatField(null=True)
    percentage_change_in_volume = models.FloatField(null=True)
    last_updated_database = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.Symbol
