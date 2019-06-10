from django.conf.urls import url

from .views import (
    PostListAPIView,
    PostCreateAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDestroyAPIView
)
app_name ='posts'

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>[\d-]+)/$', PostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d-]+)/update/$', PostUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>[\d-]+)/delete/$', PostDestroyAPIView.as_view(), name='delete')
]