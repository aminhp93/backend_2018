# chat/urls.py
from django.conf.urls import url

from . import views

app_name ='nosts'
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),

#      path('notes/all', notes_views.get_one_note, name='note-all'),
#     path('note/insert', notes_views.insert_note, name='note-insert'),
#     path('note/update', notes_views.update_note, name='note-update'),
# ]

urlpatterns = [
    url(r'^$', views.get_one_note, name='list'),
    url(r'^create/$', views.insert_note, name='create'),
    # url(r'^(?P<pk>[\d-]+)/$', PostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>[\d-]+)/update/$',views.update_note, name='update'),
    # url(r'^(?P<pk>[\d-]+)/delete/$', PostDestroyAPIView.as_view(), name='delete')
]