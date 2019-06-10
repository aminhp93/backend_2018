from django.http import JsonResponse
import requests
import json
# import socketio
# sio = socketio.Server()


# @sio.on('connect', namespace='/chat')
# def connect(sid, environ):
#     print("connect ", sid)


# @sio.on('chat message', namespace='/chat')
# def message(sid, data):
#     print("message ", data)
#     sio.emit('reply', room=sid)


# @sio.on('disconnect', namespace='/chat')
# def disconnect(sid):
#     print('disconnect ', sid)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def home(request, format=None):
    return Response({
        'posts': reverse('posts:list', request=request, format=format),
        'notes': reverse('notes:list', request=request, format=format),
        'jobs': reverse('jobs:list', request=request, format=format),
        'stocks': reverse('stocks:list', request=request, format=format),
        'posts-api': reverse('posts-api:list', request=request, format=format),
        'notes-api': reverse('notes-api:list', request=request, format=format),
        'jobs-api': reverse('jobs-api:list', request=request, format=format),
        'stocks-api': reverse('stocks-api:list', request=request, format=format),
    })
