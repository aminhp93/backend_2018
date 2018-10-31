from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import requests
from .models import HistoricalQuote


def get_historical_quote_by_symbol_and_date(request):
    # IndustryCode = "0001", Name = "Dầu khí", Index = 48.168515864163545, Date = "2018-1018T00=0", GrossMargin = 0.077352289853415218, EBITMargin = 0.029403309870910894, OperatingMargin = -0.011588368394197966, ProfitMargin = 0.0074892524338384487, QuickRatio = 1.3125721803786328, CurrentRatio = 2.154813739147512, ROE = 0.085845219129188133, ROA = 0.039955695085572313, ROIC = 0.03852252345379744, CurrentAssetsTurnover = 2.5043626554775598, InventoryTurnover = 11.511650779463015, ReceivablesTurnover = 6.3593100871694643, AssetsTurnover = 1.6190391074249442, LTDebtToEquity = -0.043307709728387614, TotalDebtToEquity = 1.2851663598905623, TotalDebtToTotalAssets = 0.53878858211492431, PS = 0.46522971559063603, PE = 12.364737439115613, PB = 1.7884069835627048, MarketCapitalization = None
    response = []
    historical_quote = HistoricalQuote.objects.all()
    i = 0
    while i < len(historical_quote):
        obj = historical_quote[i]
        insert_obj = {
            "Symbol": obj.Symbol,
            "Close": obj.Close,
            "Open": obj.Open,
            "High": obj.High,
            "Low": obj.Low,
            "Volume": obj.Volume,
            "Value": obj.Value,
            "Date": obj.Date
        }
        response.append(insert_obj)
        i += 1
    return JsonResponse({'data': response})


def delete_all_historical_quote(request):

    HistoricalQuote.objects.all().delete()
    # allSymbol = "AAA,AAM,AAV,ABC,ABI,ABR,ABT,AC4,ACB,ACC,ACE,ACL,ACM,ACS,ACV,ADC,ADP,ADS,AFC,AFX,AG1,AGF,AGM,AGP,AGR,AGX,ALT,ALV,AMC,AMD,AME,AMP,AMS,AMV,ANT,ANV,APC,APF,APG,API,APL,APP,APS,ARM,ART,ASA,ASD,ASM,ASP,AST,ATA,ATB,ATG,ATS,AUM,AVC,AVF,B82,BAB,BAL,BAX,BBC,BBM,BBS,BBT,BCC,BCE,BCG,BCM,BCP,BDB,BDC,BDF,BDG,BDP,BDT,BDW,BED,BEL,BFC,BGW,BHA,BHC,BHK,BHN,BHP,BHT,BHV,BIC,BID,BII,BIO,BKC,BLF,BLI,BLN,BLT,BLW,BMC,BMD,BMF,BMI,BMJ,BMN,BMP,BMS,BMV,BPC,BPW,BQB,BRC,BRR,BRS,BSA,BSC,BSD,BSG,BSH,BSI,BSL,BSP,BSQ,BSR,BST,BT1,BT6,BTB,BTC,BTD,BTG,BTH,BTN,BTP,BTR,BTS,BTT,BTU,BTV,BTW,BUD,BVG,BVH,BVN,BVS,BWA,BWE,BWS,BXH,C12,C21,C22,C32,C36,C47,C69,C71,C92,CAD,CAG,CAN,CAP,CAT,CAV,CBI,CBS,CC1,CC4,CCH,CCI,CCL,CCM,CCP,CCR,CCT,CCV,CDC,CDG,CDH,CDN,CDP,CDR,CE1,CEC,CEE,CEG,CEN,CEO,CER,CET,CFC,CGP,CGV,CH5,CHC,CHP,CHS,CI5,CIA,CID,CIG,CII,CIP,CJC,CKA,CKD,CKH,CKV,CLC,CLG,CLH,CLL,CLM,CLW,CLX,CMC,CMF,CMG,CMI,CMK,CMN,CMP,CMS,CMT,CMV,CMW,CMX,CNC,CNG,CNH,CNN,CNT,COM,CPC,CPH,CPI,CQT,CRC,CRE,CSC,CSM,CSV,CT3,CT6,CTA,CTB,CTC,CTD,CTF,CTG,CTI,CTN,CTP,CTR,CTS,CTT,CTW,CTX,CVC,CVH,CVN,CVT,CX8,CXH,CYC,CZC,D11,D2D,DAC,DAD,DAE,DAG,DAH,DAP,DAR,DAS,DAT,DBC,DBD,DBH,DBM,DBT,DBW,DC1,DC2,DC4,DCD,DCF,DCH,DCI,DCL,DCM,DCR,DCS,DCT,DDH,DDM,DDN,DDV,DFC,DGC,DGT,DGW,DHA,DHB,DHC,DHD,DHG,DHM,DHN,DHP,DHT,DIC,DID,DIG,DIH,DKP,DL1,DLD,DLG,DLR,DLT,DM7,DMC,DNA,DNC,DND,DNE,DNH,DNL,DNM,DNN,DNP,DNR,DNS,DNW,DNY,DOC,DOP,DP1,DP2,DP3,DPC,DPG,DPH,DPM,DPP,DPR,DPS,DQC,DRC,DRH,DRI,DRL,DS3,DSC,DSG,DSN,DSP,DSS,DST,DSV,DT4,DTA,DTC,DTD,DTG,DTI,DTK,DTL,DTN,DTT,DTV,DVC,DVH,DVN,DVP,DVW,DX2,DXG,DXL,DXP,DXV,DZM,E1VFVN30,EAD,EBS,ECI,EFI,EIB,EIC,EID,EIN,ELC,EMC,EME,EMG,EMS,EPC,EPH,EVE,EVF,EVG,EVS,FBA,FBC,FCC,FCM,FCN,FCS,FDC,FDG,FDT,FGL,FHN,FIC,FID,FIR,FIT,FLC,FMC,FOX,FPT,FRC,FRM,FRT,FSC,FSO,FT1,FTI,FTM,FTS,FUCTVGF1,FUCTVGF2,FUCVREIT,FUESSV50,G20,G36,GAS,GCB,GDT,GDW,GEG,GER,GEX,GGG,GGS,GHC,GIL,GKM,GLT,GLW,GMC,GMD,GMX,GND,GSM,GSP,GTA,GTC,GTD,GTH,GTN,GTS,GTT,GVR,GVT,H11,HAB,HAC,HAD,HAF,HAG,HAH,HAI,HAM,HAN,HAP,HAR,HAS,HAT,HAV,HAX,HBC,HBD,HBE,HBH,HBS,HBW,HC3,HCC,HCD,HCI,HCM,HCS,HCT,HD2,HDA,HDB,HDC,HDG,HDM,HDO,HDP,HDW,HEC,HEJ,HEM,HEP,HES,HEV,HFB,HFC,HFS,HFT,HFX,HGM,HGW,HHA,HHC,HHG,HHN,HHP,HHR,HHS,HHV,HID,HIG,HII,HIZ,HJC,HJS,HKB,HKP,HKT,HLA,HLB,HLC,HLD,HLE,HLG,HLR,HLS,HLY,HMC,HMG,HMH,HMS,HNA,HNB,HND,HNF,HNG,HNI,HNM,HNP,HNR,HNT,HOM,HOT,HPB,HPD,HPG,HPH,HPI,HPM,HPP,HPT,HPU,HPW,HPX,HQC,HRB,HRC,HRG,HRT,HSA,HSG,HSI,HSL,HSM,HST,HT1,HTC,HTE,HTG,HTI,HTK,HTL,HTM,HTP,HTR,HTT,HTU,HTV,HTW,HU1,HU3,HU4,HU6,HUG,HUT,HVA,HVG,HVN,HVT,HVX,HWS,I10,IBC,ICC,ICF,ICG,ICI,ICN,IDC,IDI,IDJ,IDN,IDV,IFC,IFS,IHK,IJC,IKH,ILA,ILC,ILS,IME,IMP,IN4,INC,INN,IPA,IRC,ISG,ISH,IST,ITA,ITC,ITD,ITQ,ITS,IVS,JOS,JVC,KAC,KBC,KBE,KCB,KCE,KDC,KDF,KDH,KDM,KGM,KGU,KHA,KHB,KHD,KHL,KHP,KHS,KHW,KIP,KKC,KLB,KLF,KMR,KMT,KOS,KPF,KSB,KSD,KSE,KSH,KSK,KSQ,KST,KSV,KTB,KTC,KTL,KTS,KTT,KTU,KVC,L10,L12,L14,L18,L35,L43,L44,L45,L61,L62,L63,LAF,LAI,LAS,LAW,LBC,LBE,LBM,LCC,LCD,LCG,LCM,LCS,LCW,LDG,LDP,LDW,LEC,LG9,LGC,LGL,LHC,LHG,LIC,LIG,LIX,LKW,LLM,LM3,LM7,LM8,LMC,LMH,LMI,LO5,LPB,LQN,LSS,LTC,LTG,LUT,LWS,M10,MAC,MAS,MBB,MBG,MBN,MBS,MC3,MCC,MCF,MCG,MCH,MCI,MCO,MCP,MCT,MDA,MDC,MDF,MDG,MEC,MEF,MEL,MES,MGC,MGG,MH3,MHC,MHL,MIC,MIE,MIG,MIM,MKP,MKV,MLC,MLS,MNB,MND,MPC,MPT,MPY,MQB,MQN,MRF,MSC,MSN,MSR,MST,MTA,MTC,MTG,MTH,MTL,MTM,MTP,MTS,MTV,MVB,MVC,MVN,MVY,MWG,NAC,NAF,NAG,NAP,NAS,NAU,NAV,NAW,NBB,NBC,NBE,NBP,NBR,NBT,NBW,NCP,NCS,NCT,ND2,NDC,NDF,NDN,NDP,NDT,NDX,NED,NET,NFC,NGC,NHA,NHC,NHH,NHP,NHT,NHV,NKG,NLG,NLS,NMK,NNB,NNC,NNG,NNT,NOS,NPH,NPS,NQB,NQN,NQT,NRC,NS2,NS3,NSC,NSG,NSH,NST,NT2,NTB,NTC,NTL,NTP,NTR,NTT,NTW,NUE,NVB,NVL,NVP,NVT,NWT,OCH,OGC,OIL,ONE,ONW,OPC,ORS,PAC,PAI,PAN,PBK,PBP,PC1,PCC,PCE,PCF,PCG,PCM,PCN,PCT,PDB,PDC,PDN,PDR,PDV,PEC,PEN,PEQ,PET,PFL,PGC,PGD,PGI,PGS,PGT,PGV,PHC,PHH,PHP,PHR,PIA,PIC,PID,PIS,PIT,PIV,PJC,PJS,PJT,PKR,PLA,PLC,PLP,PLX,PMB,PMC,PME,PMG,PMJ,PMP,PMS,PMT,PNC,PND,PNG,PNJ,PNT,POB,POM,POS,POT,POV,POW,PPC,PPE,PPG,PPH,PPI,PPP,PPS,PPY,PRC,PRO,PRT,PSB,PSC,PSD,PSE,PSG,PSI,PSL,PSN,PSP,PSW,PTB,PTC,PTD,PTE,PTG,PTH,PTI,PTK,PTL,PTM,PTO,PTP,PTS,PTT,PTX,PV2,PVA,PVB,PVC,PVD,PVE,PVG,PVH,PVI,PVL,PVM,PVO,PVP,PVR,PVS,PVT,PVV,PVX,PVY,PWS,PX1,PXA,PXC,PXI,PXL,PXM,PXS,PXT,PYU,QBR,QBS,QCC,QCG,QHD,QHW,QLD,QLT,QNC,QNS,QNU,QNW,QPH,QSP,QST,QTC,QTP,RAL,RAT,RBC,RCC,RCD,RCL,RDP,REE,RGC,RHN,RIC,RLC,ROS,RTB,RTH,RTS,S12,S27,S33,S4A,S55,S72,S74,S96,S99,SAB,SAC,SAF,SAL,SAM,SAP,SAS,SAV,SB1,SBA,SBD,SBH,SBL,SBM,SBS,SBT,SBV,SC5,SCC,SCD,SCI,SCJ,SCL,SCO,SCR,SCS,SCY,SD1,SD2,SD3,SD4,SD5,SD6,SD7,SD8,SD9,SDA,SDB,SDC,SDD,SDE,SDG,SDH,SDI,SDJ,SDK,SDN,SDP,SDT,SDU,SDV,SDX,SDY,SEA,SEB,SED,SEP,SFC,SFG,SFI,SFN,SGC,SGD,SGH,SGN,SGO,SGP,SGR,SGS,SGT,SHA,SHB,SHC,SHG,SHI,SHN,SHP,SHS,SHX,SIC,SID,SII,SIV,SJ1,SJC,SJD,SJE,SJF,SJG,SJM,SJS,SKG,SKH,SKN,SKV,SLC,SLS,SMA,SMB,SMC,SMN,SMT,SNC,SNZ,SON,SP2,SPA,SPB,SPC,SPD,SPH,SPI,SPM,SPP,SPV,SQC,SRA,SRB,SRC,SRF,SRT,SSC,SSF,SSG,SSI,SSM,SSN,SSU,ST8,STB,STC,STG,STK,STL,STP,STS,STT,STU,STV,STW,SUM,SVC,SVG,SVH,SVI,SVL,SVN,SVT,SWC,SZE,SZL,T12,TA3,TA6,TA9,TAC,TAP,TAW,TB8,TBC,TBD,TBN,TBT,TBX,TC6,TCB,TCD,TCH,TCI,TCJ,TCK,TCL,TCM,TCO,TCR,TCS,TCT,TCW,TDB,TDC,TDG,TDH,TDN,TDS,TDT,TDW,TEC,TEG,TEL,TET,TFC,TGG,TGP,TH1,THB,THG,THI,THN,THR,THS,THT,THU,THW,TIE,TIG,TIP,TIS,TIX,TJC,TKC,TKU,TL4,TLD,TLG,TLH,TLP,TLT,TMB,TMC,TMG,TMP,TMS,TMT,TMW,TMX,TNA,TNB,TNC,TND,TNG,TNI,TNM,TNP,TNS,TNT,TNW,TOP,TOT,TPB,TPC,TPH,TPP,TPS,TQN,TRA,TRC,TRS,TRT,TS3,TS4,TS5,TSB,TSC,TSD,TSG,TSJ,TST,TTB,TTC,TTD,TTF,TTG,TTH,TTJ,TTL,TTN,TTP,TTR,TTS,TTT,TTV,TTZ,TUG,TV1,TV2,TV3,TV4,TVA,TVB,TVC,TVD,TVG,TVM,TVN,TVP,TVS,TVT,TVU,TVW,TW3,TXM,TYA,UCT,UDC,UDJ,UEM,UIC,UMC,UNI,UPC,UPH,USC,V11,V12,V15,V21,VAF,VAT,VAV,VBC,VBG,VBH,VC1,VC2,VC3,VC5,VC6,VC7,VC9,VCA,VCB,VCC,VCE,VCF,VCG,VCI,VCM,VCP,VCR,VCS,VCT,VCW,VCX,VDL,VDM,VDN,VDP,VDS,VDT,VE1,VE2,VE3,VE4,VE8,VE9,VEA,VEC,VEE,VEF,VES,VET,VFC,VFG,VFR,VGC,VGG,VGI,VGL,VGP,VGR,VGS,VGT,VGV,VHC,VHD,VHF,VHG,VHH,VHL,VHM,VIB,VIC,VID,VIE,VIF,VIG,VIH,VIM,VIN,VIP,VIR,VIS,VIT,VIW,VIX,VJC,VKC,VKD,VKP,VLA,VLB,VLC,VLF,VLG,VLP,VLW,VMA,VMC,VMD,VMG,VMI,VMS,VNA,VNB,VNC,VND,VNE,VNF,VNG,VNH,VNI,VNL,VNM,VNP,VNR,VNS,VNT,VNX,VNY,VOC,VOS,VPA,VPB,VPC,VPD,VPG,VPH,VPI,VPK,VPR,VPS,VPW,VQC,VRC,VRE,VRG,VSA,VSC,VSE,VSF,VSG,VSH,VSI,VSM,VSN,VSP,VST,VT1,VT8,VTA,VTB,VTC,VTE,VTG,VTH,VTI,VTJ,VTL,VTM,VTO,VTS,VTV,VTX,VVN,VWS,VXB,WCS,WSB,WSS,WTC,WTN,X18,X20,X26,X77,XHC,XLV,XMD,XPH,YBC,YBM,YEG,YRC,YTC"
    # j = 0
    # while j < len(allSymbol.split(',')):
    #     symbol = allSymbol.split(',')[j]
    #     # url2 = 'https://project-2018-backend.herokuapp.com/'
    #     # requests.get(url2)
    #     print(symbol)
    #     url = 'https://svr1.fireant.vn/api/Data/Markets/HistoricalQuotes?symbol=' + \
    #         symbol + '&startDate=2017-10-8&endDate=2018-10-21'
    #     response = requests.get(url)
    #     if response.status_code == 200:
    #         i = 0
    #         while i < len(response.json()):
    #             obj = response.json()[i]
    #             new_historical_quote = HistoricalQuote()
    #             for key in obj:
    #                 if (key == 'Symbol'):
    #                     new_historical_quote.Symbol = obj['Symbol']
    #                 elif (key == 'Close'):
    #                     new_historical_quote.Close = obj['Close']
    #                 elif (key == 'Open'):
    #                     new_historical_quote.Open = obj['Open']
    #                 elif (key == 'High'):
    #                     new_historical_quote.High = obj['High']
    #                 elif (key == 'Low'):
    #                     new_historical_quote.Low = obj['Low']
    #                 elif (key == 'Volume'):
    #                     new_historical_quote.Volume = obj['Volume']
    #                 elif (key == 'Value'):
    #                     new_historical_quote.Value = obj['Value']
    #                 elif (key == 'Date'):
    #                     new_historical_quote.Date = obj['Date']
    #             new_historical_quote.save()
    #             if not new_historical_quote.id:
    #                 return JsonResponse({'data': 'false'})
    #             i += 1
    #         j += 1
    return JsonResponse({'data': 'true'})


def insert_historical_quote(request, symbol=None):
    HistoricalQuote.objects.all().delete()
    print(symbol)
    url = 'https://svr1.fireant.vn/api/Data/Markets/HistoricalQuotes?symbol=' + \
        symbol + '&startDate=2017-10-8&endDate=2018-10-23'
    response = requests.get(url)
    print(response)
    if response.status_code == 200:
        i = 0
        while i < len(response.json()):
            obj = response.json()[i]
            new_historical_quote = HistoricalQuote()
            for key in obj:
                if (key == 'Symbol'):
                    new_historical_quote.Symbol = obj['Symbol']
                elif (key == 'Close'):
                    new_historical_quote.Close = obj['Close']
                elif (key == 'Open'):
                    new_historical_quote.Open = obj['Open']
                elif (key == 'High'):
                    new_historical_quote.High = obj['High']
                elif (key == 'Low'):
                    new_historical_quote.Low = obj['Low']
                elif (key == 'Volume'):
                    new_historical_quote.Volume = obj['Volume']
                elif (key == 'Value'):
                    new_historical_quote.Value = obj['Value']
                elif (key == 'Date'):
                    new_historical_quote.Date = obj['Date']
            new_historical_quote.save()
            if not new_historical_quote.id:
                return JsonResponse({'data': 'false'})
            i += 1
    return JsonResponse({'data': symbol})
