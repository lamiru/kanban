import json
from django.core.serializers import serialize
from django.http import Http404, JsonResponse
from django.shortcuts import render
from main.models import *


def items(request):
    list_json = json.loads(serialize('json', List.objects.all()))
    card_json = json.loads(serialize('json', Card.objects.all()))

    return JsonResponse({'lists': list_json, 'cards': card_json})

def lists(request):
    list_json = json.loads(serialize('json', List.objects.all()))

    return JsonResponse({'lists': list_json})

def cards_in_list(request, pk):
    card_json = json.loads(serialize('json', Card.objects.filter(list=pk)))

    return JsonResponse({'cards': card_json})
