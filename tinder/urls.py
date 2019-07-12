# chat/urls.py
from django.conf.urls import url

from . import views

app_name = 'tinder'

urlpatterns = [
    url(r'^$', views.tinder_list, name='list'),
    url(r'^create/$', views.tinder_create, name='create'),
    url(r'^(?P<pk>[\d-]+)/$', views.tinder_detail, name='detail'),
    url(r'^(?P<pk>[\d-]+)/update/$', views.tinder_update, name='update'),
    url(r'^(?P<pk>[\d-]+)/delete/$', views.tinder_delete, name='delete'),
    url(r'^delete/all/$', views.tinder_delete_all, name='delete-all'),
    url(r'^filter/$', views.tinder_filter, name='filter'),
    url(r'^analyze/$', views.analyze, name='analyze'),
]
