from django.conf.urls import url

from .views import (
    PostListAPIView
)
app_name ='posts'

urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list')
]