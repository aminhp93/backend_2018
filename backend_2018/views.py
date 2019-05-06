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


def home(request):
    return JsonResponse({'data': 'home'})


def chat(request):
    print(dir(sio))
    return JsonResponse({'data': 'chat'})
