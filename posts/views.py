from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import requests


def test(request):
    url = 'https://www.fireant.vn/api/Data/Finance/AllIndustryFinancialInfo'
    r = requests.get(url)
    data = [
        {
            "IndustryCode": "0001",
            "Name": "Dầu khí",
            "Index": 48.168515864163545,
            "Date": "2018-10-18T00:00:00",
            "GrossMargin": 0.077352289853415218,
            "EBITMargin": 0.029403309870910894,
            "OperatingMargin": -0.011588368394197966,
            "ProfitMargin": 0.0074892524338384487,
            "QuickRatio": 1.3125721803786328,
            "CurrentRatio": 2.154813739147512,
            "ROE": 0.085845219129188133,
            "ROA": 0.039955695085572313,
            "ROIC": 0.03852252345379744,
            "CurrentAssetsTurnover": 2.5043626554775598,
            "InventoryTurnover": 11.511650779463015,
            "ReceivablesTurnover": 6.3593100871694643,
            "AssetsTurnover": 1.6190391074249442,
            "LTDebtToEquity": -0.043307709728387614,
            "TotalDebtToEquity": 1.2851663598905623,
            "TotalDebtToTotalAssets": 0.53878858211492431,
            "PS": 0.46522971559063603,
            "PE": 12.364737439115613,
            "PB": 1.7884069835627048,
            "MarketCapitalization": null
        }
    ]
    print(r)
    # return HttpResponse(html)
    return JsonResponse({'foo': 'bar'})
