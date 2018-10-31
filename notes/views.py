from django.shortcuts import render
from .models import Note
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
from django.contrib import messages
import json


@csrf_exempt
def get_one_note(request):
    note = Note.objects.first()
    if not note:
        note = Note()
        note.content = 'New note'
        note.save()
    return JsonResponse({'note': note.content})


@csrf_exempt
def insert_note(request):
    if request.method == 'POST':
        print('true')
        note = Note()
        note.content = 'note1'
        note.save()
        if not note.id:
            return JsonResponse({'data': 'Insert Failed'})
        return JsonResponse({'data': 'Insert Successfully'})
    return JsonResponse({'data': 'Invalid request'})


@csrf_exempt
def update_note(request):
    if request.method == 'POST':
        str_data = request.body.decode('utf-8')
        data = json.loads(str_data)
        print(data['note'])
        notes = Note.objects.all()
        if len(notes) == 0:
            note = Note()
        else:
            note = notes[0]
        note.content = data['note']
        note.save()
        return JsonResponse({'data': 'Update Successfully'})
    return JsonResponse({'data': 'Invalid request'})
