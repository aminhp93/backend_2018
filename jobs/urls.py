# chat/urls.py
from django.conf.urls import url

from . import views

app_name ='posts'

urlpatterns = [
    url(r'^$', views.get_all_jobs, name='list'),
    url(r'^create/$', views.create_job, name='create'),
    # url(r'^(?P<pk>[\d-]+)/$', PostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d-]+)/update/$', views.update_job, name='update'),
    # url(r'^(?P<pk>[\d-]+)/delete/$', PostDestroyAPIView.as_view(), name='delete')
    url(r'^lastjob/$', views.get_last_job, name='lastjob'),
]
