# chat/urls.py
from django.conf.urls import url

from . import views

app_name = 'stocks'

urlpatterns = [
    url(r'^$', views.stock_list, name='list'),
    url(r'^create/$', views.stock_create, name='create'),
    url(r'^(?P<pk>[\d-]+)/$', views.stock_detail, name='detail'),
    url(r'^(?P<pk>[\d-]+)/update/$', views.stock_update, name='update'),
    url(r'^(?P<pk>[\d-]+)/delete/$', views.stock_delete, name='delete'),
    url(r'^delete/all/$', views.stock_delete_all, name='delete-all'),
    url(r'^filter/$', views.stock_filter, name='filter'),
]