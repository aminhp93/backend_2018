from django.conf.urls import url

from .views import (
    TinderListAPIView,
    TinderCreateAPIView,
    TinderDetailAPIView,
    TinderUpdateAPIView,
    TinderDestroyAPIView,
    TinderDestroyAllAPIView,
)
app_name ='tinder'

urlpatterns = [
    url(r'^$', TinderListAPIView.as_view(), name='list'),
    url(r'^create/$', TinderCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>[\d-]+)/$', TinderDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d-]+)/update/$', TinderUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>[\d-]+)/delete/$', TinderDestroyAPIView.as_view(), name='delete'),
    url(r'^delete/all/$', TinderDestroyAllAPIView, name='delete'),
]