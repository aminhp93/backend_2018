from django.conf.urls import url

from .views import (
    StockListAPIView,
    StockCreateAPIView,
    StockDetailAPIView,
    StockUpdateAPIView,
    StockDestroyAPIView
)
app_name ='stocks'

urlpatterns = [
    url(r'^$', StockListAPIView.as_view(), name='list'),
    url(r'^create/$', StockCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>[\d-]+)/$', StockDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d-]+)/update/$', StockUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>[\d-]+)/delete/$', StockDestroyAPIView.as_view(), name='delete')
]