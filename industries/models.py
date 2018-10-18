from django.db import models
# Create your models here.


class Industry(models.Model):
    AssetsTurnover = models.DecimalField(max_digits=30, decimal_places=16)
    CurrentAssetsTurnover = models.DecimalField(
        max_digits=20, decimal_places=16)
    CurrentRatio = models.DecimalField(max_digits=20, decimal_places=16)
    Date = models.DateTimeField(auto_now=True, auto_now_add=False)
    EBITMargin = models.DecimalField(max_digits=20, decimal_places=16)
    GrossMargin = models.DecimalField(max_digits=20, decimal_places=16)
    Index = models.DecimalField(max_digits=20, decimal_places=16)
    IndustryCode = models.CharField(max_length=120)
    InventoryTurnover = models.DecimalField(max_digits=20, decimal_places=16)
    LTDebtToEquity = models.DecimalField(max_digits=20, decimal_places=16)
    MarketCapitalization = models.CharField(
        max_length=120,  null=True, blank=True)
    Name = models.CharField(max_length=120)
    OperatingMargin = models.DecimalField(max_digits=20, decimal_places=16)
    PB = models.DecimalField(max_digits=20, decimal_places=16)
    PE = models.DecimalField(max_digits=20, decimal_places=16)
    PS = models.DecimalField(max_digits=20, decimal_places=16)
    ProfitMargin = models.DecimalField(max_digits=20, decimal_places=16)
    QuickRatio = models.DecimalField(max_digits=20, decimal_places=16)
    ROA = models.DecimalField(max_digits=20, decimal_places=16)
    ROE = models.DecimalField(max_digits=20, decimal_places=16)
    ROIC = models.DecimalField(max_digits=20, decimal_places=16)
    ReceivablesTurnover = models.DecimalField(max_digits=20, decimal_places=16)
    TotalDebtToEquity = models.DecimalField(max_digits=20, decimal_places=16)
    TotalDebtToTotalAssets = models.DecimalField(
        max_digits=20, decimal_places=16)

    def __str__(self):
        return self.IndustryCode
