from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import requests
from industries.models import Industry


def get_all_industries(request):
    # url = 'https://www.fireant.vn/api/Data/Finance/AllIndustryFinancialInfo'
    # response = requests.get(url)
    # if response.status_code == 200:
    #     i = 0
    #     while i < 49:
    #         obj = response.json()[i]
    #         new_industry = Industry()
    #         for key in obj:
    #             if (key == 'IndustryCode'):
    #                 new_industry.IndustryCode = obj['IndustryCode']
    #             elif (key == 'Name'):
    #                 new_industry.Name = obj['Name']
    #             elif (key == 'Index'):
    #                 new_industry.Index = obj['Index']
    #             elif (key == 'Date'):
    #                 new_industry.Date = obj['Date']
    #             elif (key == 'GrossMargin'):
    #                 new_industry.GrossMargin = obj['GrossMargin']
    #             elif (key == 'EBITMargin'):
    #                 new_industry.EBITMargin = obj['EBITMargin']
    #             elif (key == 'OperatingMargin'):
    #                 new_industry.OperatingMargin = obj['OperatingMargin']
    #             elif (key == 'ProfitMargin'):
    #                 new_industry.ProfitMargin = obj['ProfitMargin']
    #             elif (key == 'QuickRatio'):
    #                 new_industry.QuickRatio = obj['QuickRatio']
    #             elif (key == 'CurrentRatio'):
    #                 new_industry.CurrentRatio = obj['CurrentRatio']
    #             elif (key == 'ROE'):
    #                 new_industry.ROE = obj['ROE']
    #             elif (key == 'ROA'):
    #                 new_industry.ROA = obj['ROA']
    #             elif (key == 'ROIC'):
    #                 new_industry.ROIC = obj['ROIC']
    #             elif (key == 'CurrentAssetsTurnover'):
    #                 new_industry.CurrentAssetsTurnover = obj['CurrentAssetsTurnover']
    #             elif (key == 'InventoryTurnover'):
    #                 new_industry.InventoryTurnover = obj['InventoryTurnover']
    #             elif (key == 'ReceivablesTurnover'):
    #                 new_industry.ReceivablesTurnover = obj['ReceivablesTurnover']
    #             elif (key == 'AssetsTurnover'):
    #                 new_industry.AssetsTurnover = obj['AssetsTurnover']
    #             elif (key == 'LTDebtToEquity'):
    #                 new_industry.LTDebtToEquity = obj['LTDebtToEquity']
    #             elif (key == 'TotalDebtToEquity'):
    #                 new_industry.TotalDebtToEquity = obj['TotalDebtToEquity']
    #             elif (key == 'TotalDebtToTotalAssets'):
    #                 new_industry.TotalDebtToTotalAssets = obj['TotalDebtToTotalAssets']
    #             elif (key == 'PS'):
    #                 new_industry.PS = obj['PS']
    #             elif (key == 'PE'):
    #                 new_industry.PE = obj['PE']
    #             elif (key == 'PB'):
    #                 new_industry.PB = obj['PB']
    #             elif (key == 'MarketCapitalization'):
    #                 new_industry.MarketCapitalization = obj['MarketCapitalization']
    #         new_industry.save()
    #         i += 1

    # # obj = {
    # IndustryCode = "0001", Name = "Dầu khí", Index = 48.168515864163545, Date = "2018-1018T00=0", GrossMargin = 0.077352289853415218, EBITMargin = 0.029403309870910894, OperatingMargin = -0.011588368394197966, ProfitMargin = 0.0074892524338384487, QuickRatio = 1.3125721803786328, CurrentRatio = 2.154813739147512, ROE = 0.085845219129188133, ROA = 0.039955695085572313, ROIC = 0.03852252345379744, CurrentAssetsTurnover = 2.5043626554775598, InventoryTurnover = 11.511650779463015, ReceivablesTurnover = 6.3593100871694643, AssetsTurnover = 1.6190391074249442, LTDebtToEquity = -0.043307709728387614, TotalDebtToEquity = 1.2851663598905623, TotalDebtToTotalAssets = 0.53878858211492431, PS = 0.46522971559063603, PE = 12.364737439115613, PB = 1.7884069835627048, MarketCapitalization = None
    # IndustryCode = '2770', Name = 'Vận tải, kho bãi', Index = 53.1508864918917, Date = '2018-10-19T00=00=00', GrossMargin = 0.16186264348074456, EBITMargin = 0.030552754474091774, OperatingMargin = 0.04472773400463437, ProfitMargin = -0.008752696402529113, QuickRatio = 2.2114038641693163, CurrentRatio = 2.348342713575727, ROE = 0.15781039538314298, ROA = 0.06882888577927866, ROIC = -0.3481886325928277, CurrentAssetsTurnover = 3.1641289224197084, InventoryTurnover = 15323.932653007038, ReceivablesTurnover = 8.317120899001651, AssetsTurnover = 1.2708265928006337, LTDebtToEquity = -0.0834165853876843, TotalDebtToEquity = 1.2781225058315417, TotalDebtToTotalAssets = 0.5386550563901009, PS = 2.4160510377219566, PE = 18.743243901958575, PB = 3.3186571762386143, MarketCapitalization = None
    # # }

    # obj = [{
    #     'IndustryCode': "0001",
    #     'Name': "Dầu khí",
    #     'Index': 48.168515864163545,
    #     'Date': "2018-10-18T00:0:0",
    #     'GrossMargin': 0.077352289853415218,
    #     'EBITMargin': 0.029403309870910894,
    #     'OperatingMargin': -0.011588368394197966,
    #     'ProfitMargin': 0.0074892524338384487,
    #     'QuickRatio': 1.3125721803786328,
    #     'CurrentRatio': 2.154813739147512,
    #     'ROE': 0.085845219129188133,
    #     'ROA': 0.039955695085572313,
    #     'ROIC': 0.03852252345379744,
    #     'CurrentAssetsTurnover': 2.5043626554775598,
    #     'InventoryTurnover': 11.511650779463015,
    #     'ReceivablesTurnover': 6.3593100871694643,
    #     'AssetsTurnover': 1.6190391074249442,
    #     'LTDebtToEquity': -0.043307709728387614,
    #     'TotalDebtToEquity': 1.2851663598905623,
    #     'TotalDebtToTotalAssets': 0.53878858211492431,
    #     'PS': 0.46522971559063603,
    #     'PE': 12.364737439115613,
    #     'PB': 1.7884069835627048,
    #     'MarketCapitalization': None
    # }
    # Industry.objects.create(obj)
    # print(Industry.objects.all())
    response = []
    all_industries = Industry.objects.all()
    i = 0
    while i < len(all_industries):
        obj = all_industries[i]
        insert_obj = {
            'IndustryCode': obj.IndustryCode,
            'Name': obj.Name,
            'Index': obj.Index,
            'Date': obj.Date,
            'GrossMargin': obj.GrossMargin,
            'EBITMargin': obj.EBITMargin,
            'OperatingMargin': obj.OperatingMargin,
            'ProfitMargin': obj.ProfitMargin,
            'QuickRatio': obj.QuickRatio,
            'CurrentRatio': obj.CurrentRatio,
            'ROE': obj.ROE,
            'ROA': obj.ROA,
            'ROIC': obj.ROIC,
            'CurrentAssetsTurnover': obj.CurrentAssetsTurnover,
            'InventoryTurnover': obj.InventoryTurnover,
            'ReceivablesTurnover': obj.ReceivablesTurnover,
            'AssetsTurnover': obj.AssetsTurnover,
            'LTDebtToEquity': obj.LTDebtToEquity,
            'TotalDebtToEquity': obj.TotalDebtToEquity,
            'TotalDebtToTotalAssets': obj.TotalDebtToTotalAssets,
            'PS': obj.PS,
            'PE': obj.PE,
            'PB': obj.PB,
            'MarketCapitalization': obj.MarketCapitalization
        }
        response.append(insert_obj)
        i += 1
    return JsonResponse({'data': response})


def insert_all_industries(request):
    url = 'https://www.fireant.vn/api/Data/Finance/AllIndustryFinancialInfo'
    response = requests.get(url)
    if response.status_code == 200:
        i = 0
        while i < 49:
            obj = response.json()[i]
            new_industry = Industry()
            for key in obj:
                if (key == 'IndustryCode'):
                    new_industry.IndustryCode = obj['IndustryCode']
                elif (key == 'Name'):
                    new_industry.Name = obj['Name']
                elif (key == 'Index'):
                    new_industry.Index = obj['Index']
                elif (key == 'Date'):
                    new_industry.Date = obj['Date']
                elif (key == 'GrossMargin'):
                    new_industry.GrossMargin = obj['GrossMargin']
                elif (key == 'EBITMargin'):
                    new_industry.EBITMargin = obj['EBITMargin']
                elif (key == 'OperatingMargin'):
                    new_industry.OperatingMargin = obj['OperatingMargin']
                elif (key == 'ProfitMargin'):
                    new_industry.ProfitMargin = obj['ProfitMargin']
                elif (key == 'QuickRatio'):
                    new_industry.QuickRatio = obj['QuickRatio']
                elif (key == 'CurrentRatio'):
                    new_industry.CurrentRatio = obj['CurrentRatio']
                elif (key == 'ROE'):
                    new_industry.ROE = obj['ROE']
                elif (key == 'ROA'):
                    new_industry.ROA = obj['ROA']
                elif (key == 'ROIC'):
                    new_industry.ROIC = obj['ROIC']
                elif (key == 'CurrentAssetsTurnover'):
                    new_industry.CurrentAssetsTurnover = obj['CurrentAssetsTurnover']
                elif (key == 'InventoryTurnover'):
                    new_industry.InventoryTurnover = obj['InventoryTurnover']
                elif (key == 'ReceivablesTurnover'):
                    new_industry.ReceivablesTurnover = obj['ReceivablesTurnover']
                elif (key == 'AssetsTurnover'):
                    new_industry.AssetsTurnover = obj['AssetsTurnover']
                elif (key == 'LTDebtToEquity'):
                    new_industry.LTDebtToEquity = obj['LTDebtToEquity']
                elif (key == 'TotalDebtToEquity'):
                    new_industry.TotalDebtToEquity = obj['TotalDebtToEquity']
                elif (key == 'TotalDebtToTotalAssets'):
                    new_industry.TotalDebtToTotalAssets = obj['TotalDebtToTotalAssets']
                elif (key == 'PS'):
                    new_industry.PS = obj['PS']
                elif (key == 'PE'):
                    new_industry.PE = obj['PE']
                elif (key == 'PB'):
                    new_industry.PB = obj['PB']
                elif (key == 'MarketCapitalization'):
                    new_industry.MarketCapitalization = obj['MarketCapitalization']
            new_industry.save()
            i += 1
