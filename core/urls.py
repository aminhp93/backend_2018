# chat/urls.py
from django.conf.urls import url

from . import views

app_name = 'core'

urlpatterns = [
    # url(r'^$', views.note_list, name='list'),
    url(r'^$', views.get_last_updated_time, name='last_updated_time'),
    url(r'^update/$', views.update, name='update'),
    # url(r'^(?P<pk>[\d-]+)/$', views.note_detail, name='detail'),
    # url(r'^(?P<pk>[\d-]+)/update/$', views.note_update, name='update'),
    # url(r'^(?P<pk>[\d-]+)/delete/$', views.note_delete, name='delete')
]
