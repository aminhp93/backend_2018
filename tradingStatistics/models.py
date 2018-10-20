from django.db import models
# Create your models here.


class TradingStatistic(models.Model):
    Symbol = models.CharField(max_length=120)
    Exchange = models.CharField(max_length=120)
    AvgPrice5d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgVolume5d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgPrice10d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgVolume10d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgPrice20d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgVolume20d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    HighPrice1w = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    LowPrice1w = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    HighPrice1m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    LowPrice1m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    HighPrice3m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    LowPrice3m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    HighPrice6m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    LowPrice6m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    HighPrice1y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    LowPrice1y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    HighPrice2y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    LowPrice2y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    HighPrice3y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    LowPrice3y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    HighPrice5y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    LowPrice5y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    PriceChange1w = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    PriceChange1m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    PriceChange3m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    PriceChange6m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    PriceChange1y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    PriceChange2y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    PriceChange3y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    PriceChange5y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    Date = models.DateTimeField(auto_now=True, auto_now_add=False)
    BuyCount1w = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    SellCount1w = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    BuyQuantity1w = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    SellQuantity1w = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    BuyCount1m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    SellCount1m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    BuyQuantity1m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    SellQuantity1m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    BuyCount3m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    SellCount3m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    BuyQuantity3m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    SellQuantity3m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    BuyCount6m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    SellCount6m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    BuyQuantity6m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    SellQuantity6m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    BuyCount1y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    SellCount1y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    BuyQuantity1y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    SellQuantity1y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    BuyCount2y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    SellCount2y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    BuyQuantity2y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    SellQuantity2y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    BuyCount3y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    SellCount3y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    BuyQuantity3y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    SellQuantity3y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    BuyCount5y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    SellCount5y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    BuyQuantity5y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    SellQuantity5y = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgTradingSpeed10d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgTradingSpeed3m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    SharesOutStanding = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgPrice4d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgPrice9d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgPrice14d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgPrice15d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgPrice19d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgPrice44d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgPrice45d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgVolume4d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgVolume9d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgVolume14d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgVolume15d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgVolume19d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgVolume44d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgVolume45d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgVolume3m = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    StdEV19d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    StdEV20d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    EMA5d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    EMA10d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    EMA15d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    EMA20d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    EMA45d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    DEMA5d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    DEMA10d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    DEMA15d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    DEMA20d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    DEMA45d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    TEMA5d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    TEMA10d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    TEMA15d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    TEMA20d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    TEMA45d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    AvgGain14d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgLoss14d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    LastPriceClose = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    LastPriceHigh = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    LastPriceLow = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    LastDealVolume = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    AvgTypPrice13d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    PositiveMF13d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    NegativeMF13d = models.DecimalField(
        max_digits=30, decimal_places=16, null=True)
    EMA12d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    EMA26d = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    RS = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    Beta = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    Price1w = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    Price1m = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    Price3m = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    Price6m = models.DecimalField(max_digits=30, decimal_places=16, null=True)
    Price1y = models.DecimalField(max_digits=30, decimal_places=16, null=True)

    def __str__(self):
        return self.Symbol
