# chat/urls.py
from django.conf.urls import url

from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.job_list, name='list'),
    url(r'^create/$', views.job_create, name='create'),
    url(r'^(?P<pk>[\d-]+)/$', views.job_detail, name='detail'),
    url(r'^(?P<pk>[\d-]+)/update/$', views.job_update, name='update'),
    url(r'^(?P<pk>[\d-]+)/delete/$', views.job_delete, name='delete'),
    url(r'^last/$', views.job_last, name='last'),
]
