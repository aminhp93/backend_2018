from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

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

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1hSlHIs1kdoDK1arTdgmaD-5Zt4sHOcCUNTBOCgavMIw'
SAMPLE_RANGE_NAME = 'C5:C12'


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
        'tinder-api': reverse('tinder-api:list', request=request, format=format),
    })


@api_view(['GET'])
def googlesheet(request):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print(values)
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print(row)
            # print('%s, %s' % (row[0], row[1]))

    return Response({
        'data': values
    })
