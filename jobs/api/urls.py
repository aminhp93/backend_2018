from django.conf.urls import url

from .views import (
    JobListAPIView,
    JobCreateAPIView,
    JobDetailAPIView,
    JobUpdateAPIView,
    JobDestroyAPIView
)
app_name = 'jobs'

urlpatterns = [
    url(r'^$', JobListAPIView.as_view(), name='list'),
    url(r'^create/$', JobCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>[\d-]+)/$', JobDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d-]+)/update/$',
        JobUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>[\d-]+)/delete/$',
        JobDestroyAPIView.as_view(), name='delete')
]
