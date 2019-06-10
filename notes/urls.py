# chat/urls.py
from django.conf.urls import url

from . import views

app_name = 'notes'

urlpatterns = [
    url(r'^$', views.note_list, name='list'),
    url(r'^create/$', views.note_create, name='create'),
    url(r'^(?P<pk>[\d-]+)/$', views.note_detail, name='detail'),
    url(r'^(?P<pk>[\d-]+)/update/$', views.note_update, name='update'),
    url(r'^(?P<pk>[\d-]+)/delete/$', views.note_delete, name='delete')
]
