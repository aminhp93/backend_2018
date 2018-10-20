from django.db import models
# Create your models here.


class Industry(models.Model):
    AssetsTurnover = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    CurrentAssetsTurnover = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    CurrentRatio = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    Date = models.DateTimeField(auto_now=True, auto_now_add=False)
    EBITMargin = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    GrossMargin = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    Index = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    IndustryCode = models.CharField(max_length=120)
    InventoryTurnover = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    LTDebtToEquity = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    MarketCapitalization = models.CharField(
        max_length=120,  null=True, blank=True)
    Name = models.CharField(max_length=120)
    OperatingMargin = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    PB = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    PE = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    PS = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    ProfitMargin = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    QuickRatio = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    ROA = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    ROE = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    ROIC = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    ReceivablesTurnover = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    TotalDebtToEquity = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    TotalDebtToTotalAssets = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)

    def __str__(self):
        return self.IndustryCode
