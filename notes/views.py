from django.shortcuts import render
from .models import Note
# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
from django.contrib import messages


def get_one_note(request):
    print(random.randint(1, 101))
    note = Note.objects.first()
    if not note:
        return JsonResponse({'note': 'NO NOTE'})
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
        print('true')
        print(request.body, dir(request.body), request.body.decode)
        note = Note.objects.first()
        note.content = random.randint(1, 101)
        note.save()
        print(messages)
        if not note.id:
            return JsonResponse({'data': 'Insert Failed'})
        return JsonResponse({'data': 'Insert Successfully'})
    return JsonResponse({'data': 'Invalid request'})
