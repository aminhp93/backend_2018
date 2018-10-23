"""backend_2018 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from .views import home
from industries import views as industries_views
from tradingStatistics import views as trading_statistics_views
from historicalQuotes import views as historical_quotes_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('all-indudstries', industries_views.get_all_industries,
         name="all-indudstries"),
    path('all-indudstries/insert', industries_views.insert_all_industries,
         name='all-indudstries-insert'),
    path('trading-statistic', trading_statistics_views.get_trading_statistic,
         name="trading-statistic"),
    path('trading-statistic/insert', trading_statistics_views.insert_trading_statistic,
         name='trading-statistic-insert'),
    path('historical-quote', historical_quotes_views.get_historical_quote_by_symbol_and_date,
         name="historical-quote"),
    path('historical-quote/delete/all', historical_quotes_views.delete_all_historical_quote,
         name='historical-quote-delete-all'),
    path('historical-quote/insert/<symbol>/', historical_quotes_views.insert_historical_quote,
         name='historical-quote-insert'),
]
