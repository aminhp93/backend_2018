from django.shortcuts import render
from .models import Note
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
from django.contrib import messages
import json


@csrf_exempt
def note_list(request):
    note = Note.objects.first()
    if not note:
        note = Note()
        note.content = 'New note'
        note.save()
    return JsonResponse({'note': note.content})


@csrf_exempt
def note_create(request):
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
def note_detail(request, pk):
    return JsonResponse({'data': 'detail'})


@csrf_exempt
def note_update(request, pk):
    print(request, request.body.decode('utf-8'))
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        if not 'note' in data:
            return JsonResponse({'data': 'Invalid data'})
        notes = Note.objects.all()
        if len(notes) == 0:
            note = Note()
        else:
            note = notes[0]
        note.content = data['note']
        note.save()
        return JsonResponse({'data': 'Update Successfully'})
    return JsonResponse({'data': 'Invalid request'})


@csrf_exempt
def note_delete(request, pk):
    if request.method == 'POST':
        return JsonResponse({'data': 'delete'})
    return JsonResponse({'data': 'Invalid request'})
