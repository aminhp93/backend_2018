from django.db import models

# Create your models here.


class HistoricalQuote(models.Model):
    Symbol = models.CharField(max_length=120)
    Close = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    Open = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    High = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    Low = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    Volume = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    Value = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    Date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.Symbol + str(self.Date)
