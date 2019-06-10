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
    url(r'^chat/', include('chat.urls', namespace='chat')),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^notes/', include('notes.urls', namespace='notes')),
    url(r'^jobs/', include('jobs.urls', namespace='jobs')),
    url(r'^stocks/', include('stocks.urls', namespace='stocks')),
    url(r'^api/posts/', include('posts.api.urls', namespace='posts-api')),
    url(r'^api/notes/', include('notes.api.urls', namespace='notes-api')),
    url(r'^api/jobs/', include('jobs.api.urls', namespace='jobs-api')),
    url(r'^api/stocks/', include('stocks.api.urls', namespace='stocks-api')),
]
