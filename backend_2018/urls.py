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

from .views import home, chat
from industries import views as industries_views
from tradingStatistics import views as trading_statistics_views
from historicalQuotes import views as historical_quotes_views
from posts import views as posts_views
from notes import views as notes_views
from stocks import views as stocks_views
from jobs import views as jobs_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('stocks/all', stocks_views.get_all_stocks, name='all-stocks'),
    path('stock/create', stocks_views.create_stock, name='stock-create'),
    path('stock/update', stocks_views.update_stock, name='stock-update'),
    path('stock/delete/all', stocks_views.delete_all_stocks, name='stock-delete-all'),
    path('stocks/quickFilteredStocks', stocks_views.get_quick_filtered_stocks, name='quick-filtered-stocks'),
    path('stocks/filter', stocks_views.filter_stock, name='stock-filter'),
    url(r'^api/posts/', include('posts.api.urls', namespace='posts-api')),
    url(r'^api/stocks/', include('stocks.api.urls', namespace='stocks-api')),
    url(r'^chat/', include('chat.urls', namespace='chat')),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^notes/', include('notes.urls', namespace='notes')),
    url(r'^jobs/', include('jobs.urls', namespace='jobs'))
]
