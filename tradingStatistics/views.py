from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import requests
from .models import TradingStatistic


def get_trading_statistic(request):
    response = []
    tradingStatistic = TradingStatistic.objects.all()
    i = 0
    while i < len(tradingStatistic):
        obj = tradingStatistic[i]
        insert_obj = {
            "Symbol": obj.Symbol,
            "Exchange": obj.Exchange,
            "AvgPrice5d": obj.AvgPrice5d,
            "AvgVolume5d": obj.AvgVolume5d,
            "AvgPrice10d": obj.AvgPrice10d,
            "AvgVolume10d": obj.AvgVolume10d,
            "AvgPrice20d": obj.AvgPrice20d,
            "AvgVolume20d": obj.AvgVolume20d,
            "HighPrice1w": obj.HighPrice1w,
            "LowPrice1w": obj.LowPrice1w,
            "HighPrice1m": obj.HighPrice1m,
            "LowPrice1m": obj.LowPrice1m,
            "HighPrice3m": obj.HighPrice3m,
            "LowPrice3m": obj.LowPrice3m,
            "HighPrice6m": obj.HighPrice6m,
            "LowPrice6m": obj.LowPrice6m,
            "HighPrice1y": obj.HighPrice1y,
            "LowPrice1y": obj.LowPrice1y,
            "HighPrice2y": obj.HighPrice2y,
            "LowPrice2y": obj.LowPrice2y,
            "HighPrice3y": obj.HighPrice3y,
            "LowPrice3y": obj.LowPrice3y,
            "HighPrice5y": obj.HighPrice5y,
            "LowPrice5y": obj.LowPrice5y,
            "PriceChange1w": obj.PriceChange1w,
            "PriceChange1m": obj.PriceChange1m,
            "PriceChange3m": obj.PriceChange3m,
            "PriceChange6m": obj.PriceChange6m,
            "PriceChange1y": obj.PriceChange1y,
            "PriceChange2y": obj.PriceChange2y,
            "PriceChange3y": obj.PriceChange3y,
            "PriceChange5y": obj.PriceChange5y,
            "Date": obj.Date,
            "BuyCount1w": obj.BuyCount1w,
            "SellCount1w": obj.SellCount1w,
            "BuyQuantity1w": obj.BuyQuantity1w,
            "SellQuantity1w": obj.SellQuantity1w,
            "BuyCount1m": obj.BuyCount1m,
            "SellCount1m": obj.SellCount1m,
            "BuyQuantity1m": obj.BuyQuantity1m,
            "SellQuantity1m": obj.SellQuantity1m,
            "BuyCount3m": obj.BuyCount3m,
            "SellCount3m": obj.SellCount3m,
            "BuyQuantity3m": obj.BuyQuantity3m,
            "SellQuantity3m": obj.SellQuantity3m,
            "BuyCount6m": obj.BuyCount6m,
            "SellCount6m": obj.SellCount6m,
            "BuyQuantity6m": obj.BuyQuantity6m,
            "SellQuantity6m": obj.SellQuantity6m,
            "BuyCount1y": obj.BuyCount1y,
            "SellCount1y": obj.SellCount1y,
            "BuyQuantity1y": obj.BuyQuantity1y,
            "SellQuantity1y": obj.SellQuantity1y,
            "BuyCount2y": obj.BuyCount2y,
            "SellCount2y": obj.SellCount2y,
            "BuyQuantity2y": obj.BuyQuantity2y,
            "SellQuantity2y": obj.SellQuantity2y,
            "BuyCount3y": obj.BuyCount3y,
            "SellCount3y": obj.SellCount3y,
            "BuyQuantity3y": obj.BuyQuantity3y,
            "SellQuantity3y": obj.SellQuantity3y,
            "BuyCount5y": obj.BuyCount5y,
            "SellCount5y": obj.SellCount5y,
            "BuyQuantity5y": obj.BuyQuantity5y,
            "SellQuantity5y": obj.SellQuantity5y,
            "AvgTradingSpeed10d": obj.AvgTradingSpeed10d,
            "AvgTradingSpeed3m": obj.AvgTradingSpeed3m,
            "SharesOutStanding": obj.SharesOutStanding,
            "AvgPrice4d": obj.AvgPrice4d,
            "AvgPrice9d": obj.AvgPrice9d,
            "AvgPrice14d": obj.AvgPrice14d,
            "AvgPrice15d": obj.AvgPrice15d,
            "AvgPrice19d": obj.AvgPrice19d,
            "AvgPrice44d": obj.AvgPrice44d,
            "AvgPrice45d": obj.AvgPrice45d,
            "AvgVolume4d": obj.AvgVolume4d,
            "AvgVolume9d": obj.AvgVolume9d,
            "AvgVolume14d": obj.AvgVolume14d,
            "AvgVolume15d": obj.AvgVolume15d,
            "AvgVolume19d": obj.AvgVolume19d,
            "AvgVolume44d": obj.AvgVolume44d,
            "AvgVolume45d": obj.AvgVolume45d,
            "AvgVolume3m": obj.AvgVolume3m,
            "StdEV19d": obj.StdEV19d,
            "StdEV20d": obj.StdEV20d,
            "EMA5d": obj.EMA5d,
            "EMA10d": obj.EMA10d,
            "EMA15d": obj.EMA15d,
            "EMA20d": obj.EMA20d,
            "EMA45d": obj.EMA45d,
            "DEMA5d": obj.DEMA5d,
            "DEMA10d": obj.DEMA10d,
            "DEMA15d": obj.DEMA15d,
            "DEMA20d": obj.DEMA20d,
            "DEMA45d": obj.DEMA45d,
            "TEMA5d": obj.TEMA5d,
            "TEMA10d": obj.TEMA10d,
            "TEMA15d": obj.TEMA15d,
            "TEMA20d": obj.TEMA20d,
            "TEMA45d": obj.TEMA45d,
            "AvgGain14d": obj.AvgGain14d,
            "AvgLoss14d": obj.AvgLoss14d,
            "LastPriceClose": obj.LastPriceClose,
            "LastPriceHigh": obj.LastPriceHigh,
            "LastPriceLow": obj.LastPriceLow,
            "LastDealVolume": obj.LastDealVolume,
            "AvgTypPrice13d": obj.AvgTypPrice13d,
            "PositiveMF13d": obj.PositiveMF13d,
            "NegativeMF13d": obj.NegativeMF13d,
            "EMA12d": obj.EMA12d,
            "EMA26d": obj.EMA26d,
            "RS": obj.RS,
            "Beta": obj.Beta,
            "Price1w": obj.Price1w,
            "Price1m": obj.Price1m,
            "Price3m": obj.Price3m,
            "Price6m": obj.Price6m,
            "Price1y": obj.Price1y
        }
        response.append(insert_obj)
        i += 1
    return JsonResponse({'data': response})


def insert_trading_statistic(request):
    TradingStatistic.objects.all().delete()
    url = 'https://svr2.fireant.vn/api/Data/Markets/TradingStatistic'
    insert = 'false'
    response = requests.get(url)
    if response.status_code == 200:
        i = 0
        while i < len(response.json()):
            obj = response.json()[i]
            new_trading_statistic = TradingStatistic()
            for key in obj:
                if key == "Symbol":
                    new_trading_statistic.Symbol = obj['Symbol']
                elif key == "Exchange":
                    new_trading_statistic.Exchange = obj['Exchange']
                elif key == "AvgPrice5d":
                    new_trading_statistic.AvgPrice5d = obj['AvgPrice5d']
                elif key == "AvgVolume5d":
                    new_trading_statistic.AvgVolume5d = obj['AvgVolume5d']
                elif key == "AvgPrice10d":
                    new_trading_statistic.AvgPrice10d = obj['AvgPrice10d']
                elif key == "AvgVolume10d":
                    new_trading_statistic.AvgVolume10d = obj['AvgVolume10d']
                elif key == "AvgPrice20d":
                    new_trading_statistic.AvgPrice20d = obj['AvgPrice20d']
                elif key == "AvgVolume20d":
                    new_trading_statistic.AvgVolume20d = obj['AvgVolume20d']
                elif key == "HighPrice1w":
                    new_trading_statistic.HighPrice1w = obj['HighPrice1w']
                elif key == "LowPrice1w":
                    new_trading_statistic.LowPrice1w = obj['LowPrice1w']
                elif key == "HighPrice1m":
                    new_trading_statistic.HighPrice1m = obj['HighPrice1m']
                elif key == "LowPrice1m":
                    new_trading_statistic.LowPrice1m = obj['LowPrice1m']
                elif key == "HighPrice3m":
                    new_trading_statistic.HighPrice3m = obj['HighPrice3m']
                elif key == "LowPrice3m":
                    new_trading_statistic.LowPrice3m = obj['LowPrice3m']
                elif key == "HighPrice6m":
                    new_trading_statistic.HighPrice6m = obj['HighPrice6m']
                elif key == "LowPrice6m":
                    new_trading_statistic.LowPrice6m = obj['LowPrice6m']
                elif key == "HighPrice1y":
                    new_trading_statistic.HighPrice1y = obj['HighPrice1y']
                elif key == "LowPrice1y":
                    new_trading_statistic.LowPrice1y = obj['LowPrice1y']
                elif key == "HighPrice2y":
                    new_trading_statistic.HighPrice2y = obj['HighPrice2y']
                elif key == "LowPrice2y":
                    new_trading_statistic.LowPrice2y = obj['LowPrice2y']
                elif key == "HighPrice3y":
                    new_trading_statistic.HighPrice3y = obj['HighPrice3y']
                elif key == "LowPrice3y":
                    new_trading_statistic.LowPrice3y = obj['LowPrice3y']
                elif key == "HighPrice5y":
                    new_trading_statistic.HighPrice5y = obj['HighPrice5y']
                elif key == "LowPrice5y":
                    new_trading_statistic.LowPrice5y = obj['LowPrice5y']
                elif key == "PriceChange1w":
                    new_trading_statistic.PriceChange1w = obj['PriceChange1w']
                elif key == "PriceChange1m":
                    new_trading_statistic.PriceChange1m = obj['PriceChange1m']
                elif key == "PriceChange3m":
                    new_trading_statistic.PriceChange3m = obj['PriceChange3m']
                elif key == "PriceChange6m":
                    new_trading_statistic.PriceChange6m = obj['PriceChange6m']
                elif key == "PriceChange1y":
                    new_trading_statistic.PriceChange1y = obj['PriceChange1y']
                elif key == "PriceChange2y":
                    new_trading_statistic.PriceChange2y = obj['PriceChange2y']
                elif key == "PriceChange3y":
                    new_trading_statistic.PriceChange3y = obj['PriceChange3y']
                elif key == "PriceChange5y":
                    new_trading_statistic.PriceChange5y = obj['PriceChange5y']
                elif key == "Date":
                    new_trading_statistic.Date = obj['Date']
                elif key == "BuyCount1w":
                    new_trading_statistic.BuyCount1w = obj['BuyCount1w']
                elif key == "SellCount1w":
                    new_trading_statistic.SellCount1w = obj['SellCount1w']
                elif key == "BuyQuantity1w":
                    new_trading_statistic.BuyQuantity1w = obj['BuyQuantity1w']
                elif key == "SellQuantity1w":
                    new_trading_statistic.SellQuantity1w = obj['SellQuantity1w']
                elif key == "BuyCount1m":
                    new_trading_statistic.BuyCount1m = obj['BuyCount1m']
                elif key == "SellCount1m":
                    new_trading_statistic.SellCount1m = obj['SellCount1m']
                elif key == "BuyQuantity1m":
                    new_trading_statistic.BuyQuantity1m = obj['BuyQuantity1m']
                elif key == "SellQuantity1m":
                    new_trading_statistic.SellQuantity1m = obj['SellQuantity1m']
                elif key == "BuyCount3m":
                    new_trading_statistic.BuyCount3m = obj['BuyCount3m']
                elif key == "SellCount3m":
                    new_trading_statistic.SellCount3m = obj['SellCount3m']
                elif key == "BuyQuantity3m":
                    new_trading_statistic.BuyQuantity3m = obj['BuyQuantity3m']
                elif key == "SellQuantity3m":
                    new_trading_statistic.SellQuantity3m = obj['SellQuantity3m']
                elif key == "BuyCount6m":
                    new_trading_statistic.BuyCount6m = obj['BuyCount6m']
                elif key == "SellCount6m":
                    new_trading_statistic.SellCount6m = obj['SellCount6m']
                elif key == "BuyQuantity6m":
                    new_trading_statistic.BuyQuantity6m = obj['BuyQuantity6m']
                elif key == "SellQuantity6m":
                    new_trading_statistic.SellQuantity6m = obj['SellQuantity6m']
                elif key == "BuyCount1y":
                    new_trading_statistic.BuyCount1y = obj['BuyCount1y']
                elif key == "SellCount1y":
                    new_trading_statistic.SellCount1y = obj['SellCount1y']
                elif key == "BuyQuantity1y":
                    new_trading_statistic.BuyQuantity1y = obj['BuyQuantity1y']
                elif key == "SellQuantity1y":
                    new_trading_statistic.SellQuantity1y = obj['SellQuantity1y']
                elif key == "BuyCount2y":
                    new_trading_statistic.BuyCount2y = obj['BuyCount2y']
                elif key == "SellCount2y":
                    new_trading_statistic.SellCount2y = obj['SellCount2y']
                elif key == "BuyQuantity2y":
                    new_trading_statistic.BuyQuantity2y = obj['BuyQuantity2y']
                elif key == "SellQuantity2y":
                    new_trading_statistic.SellQuantity2y = obj['SellQuantity2y']
                elif key == "BuyCount3y":
                    new_trading_statistic.BuyCount3y = obj['BuyCount3y']
                elif key == "SellCount3y":
                    new_trading_statistic.SellCount3y = obj['SellCount3y']
                elif key == "BuyQuantity3y":
                    new_trading_statistic.BuyQuantity3y = obj['BuyQuantity3y']
                elif key == "SellQuantity3y":
                    new_trading_statistic.SellQuantity3y = obj['SellQuantity3y']
                elif key == "BuyCount5y":
                    new_trading_statistic.BuyCount5y = obj['BuyCount5y']
                elif key == "SellCount5y":
                    new_trading_statistic.SellCount5y = obj['SellCount5y']
                elif key == "BuyQuantity5y":
                    new_trading_statistic.BuyQuantity5y = obj['BuyQuantity5y']
                elif key == "SellQuantity5y":
                    new_trading_statistic.SellQuantity5y = obj['SellQuantity5y']
                elif key == "AvgTradingSpeed10d":
                    new_trading_statistic.AvgTradingSpeed10d = obj['AvgTradingSpeed10d']
                elif key == "AvgTradingSpeed3m":
                    new_trading_statistic.AvgTradingSpeed3m = obj['AvgTradingSpeed3m']
                elif key == "SharesOutStanding":
                    new_trading_statistic.SharesOutStanding = obj['SharesOutStanding']
                elif key == "AvgPrice4d":
                    new_trading_statistic.AvgPrice4d = obj['AvgPrice4d']
                elif key == "AvgPrice9d":
                    new_trading_statistic.AvgPrice9d = obj['AvgPrice9d']
                elif key == "AvgPrice14d":
                    new_trading_statistic.AvgPrice14d = obj['AvgPrice14d']
                elif key == "AvgPrice15d":
                    new_trading_statistic.AvgPrice15d = obj['AvgPrice15d']
                elif key == "AvgPrice19d":
                    new_trading_statistic.AvgPrice19d = obj['AvgPrice19d']
                elif key == "AvgPrice44d":
                    new_trading_statistic.AvgPrice44d = obj['AvgPrice44d']
                elif key == "AvgPrice45d":
                    new_trading_statistic.AvgPrice45d = obj['AvgPrice45d']
                elif key == "AvgVolume4d":
                    new_trading_statistic.AvgVolume4d = obj['AvgVolume4d']
                elif key == "AvgVolume9d":
                    new_trading_statistic.AvgVolume9d = obj['AvgVolume9d']
                elif key == "AvgVolume14d":
                    new_trading_statistic.AvgVolume14d = obj['AvgVolume14d']
                elif key == "AvgVolume15d":
                    new_trading_statistic.AvgVolume15d = obj['AvgVolume15d']
                elif key == "AvgVolume19d":
                    new_trading_statistic.AvgVolume19d = obj['AvgVolume19d']
                elif key == "AvgVolume44d":
                    new_trading_statistic.AvgVolume44d = obj['AvgVolume44d']
                elif key == "AvgVolume45d":
                    new_trading_statistic.AvgVolume45d = obj['AvgVolume45d']
                elif key == "AvgVolume3m":
                    new_trading_statistic.AvgVolume3m = obj['AvgVolume3m']
                elif key == "StdEV19d":
                    new_trading_statistic.StdEV19d = obj['StdEV19d']
                elif key == "StdEV20d":
                    new_trading_statistic.StdEV20d = obj['StdEV20d']
                elif key == "EMA5d":
                    new_trading_statistic.EMA5d = obj['EMA5d']
                elif key == "EMA10d":
                    new_trading_statistic.EMA10d = obj['EMA10d']
                elif key == "EMA15d":
                    new_trading_statistic.EMA15d = obj['EMA15d']
                elif key == "EMA20d":
                    new_trading_statistic.EMA20d = obj['EMA20d']
                elif key == "EMA45d":
                    new_trading_statistic.EMA45d = obj['EMA45d']
                elif key == "DEMA5d":
                    new_trading_statistic.DEMA5d = obj['DEMA5d']
                elif key == "DEMA10d":
                    new_trading_statistic.DEMA10d = obj['DEMA10d']
                elif key == "DEMA15d":
                    new_trading_statistic.DEMA15d = obj['DEMA15d']
                elif key == "DEMA20d":
                    new_trading_statistic.DEMA20d = obj['DEMA20d']
                elif key == "DEMA45d":
                    new_trading_statistic.DEMA45d = obj['DEMA45d']
                elif key == "TEMA5d":
                    new_trading_statistic.TEMA5d = obj['TEMA5d']
                elif key == "TEMA10d":
                    new_trading_statistic.TEMA10d = obj['TEMA10d']
                elif key == "TEMA15d":
                    new_trading_statistic.TEMA15d = obj['TEMA15d']
                elif key == "TEMA20d":
                    new_trading_statistic.TEMA20d = obj['TEMA20d']
                elif key == "TEMA45d":
                    new_trading_statistic.TEMA45d = obj['TEMA45d']
                elif key == "AvgGain14d":
                    new_trading_statistic.AvgGain14d = obj['AvgGain14d']
                elif key == "AvgLoss14d":
                    new_trading_statistic.AvgLoss14d = obj['AvgLoss14d']
                elif key == "LastPriceClose":
                    new_trading_statistic.LastPriceClose = obj['LastPriceClose']
                elif key == "LastPriceHigh":
                    new_trading_statistic.LastPriceHigh = obj['LastPriceHigh']
                elif key == "LastPriceLow":
                    new_trading_statistic.LastPriceLow = obj['LastPriceLow']
                elif key == "LastDealVolume":
                    new_trading_statistic.LastDealVolume = obj['LastDealVolume']
                elif key == "AvgTypPrice13d":
                    new_trading_statistic.AvgTypPrice13d = obj['AvgTypPrice13d']
                elif key == "PositiveMF13d":
                    new_trading_statistic.PositiveMF13d = obj['PositiveMF13d']
                elif key == "NegativeMF13d":
                    new_trading_statistic.NegativeMF13d = obj['NegativeMF13d']
                elif key == "EMA12d":
                    new_trading_statistic.EMA12d = obj['EMA12d']
                elif key == "EMA26d":
                    new_trading_statistic.EMA26d = obj['EMA26d']
                elif key == "RS":
                    new_trading_statistic.RS = obj['RS']
                elif key == "Beta":
                    new_trading_statistic.Beta = obj['Beta']
                elif key == "Price1w":
                    new_trading_statistic.Price1w = obj['Price1w']
                elif key == "Price1m":
                    new_trading_statistic.Price1m = obj['Price1m']
                elif key == "Price3m":
                    new_trading_statistic.Price3m = obj['Price3m']
                elif key == "Price6m":
                    new_trading_statistic.Price6m = obj['Price6m']
                elif key == "Price1y":
                    new_trading_statistic.Price1y = obj['Price1y']
                new_trading_statistic.save()
                if new_trading_statistic.id:
                    insert = 'true'
                else:
                    insert = 'false'
                i += 1
        if (insert == 'true'):
            return JsonResponse({'data': 'true'})
        else:
            return JsonResponse({'data': 'false'})
