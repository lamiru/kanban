import json
from django.core.serializers import serialize
from django.http import Http404, JsonResponse, QueryDict
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from main.models import *


def items(request):
    list_json = json.loads(serialize('json', List.objects.all()))
    card_json = json.loads(serialize('json', Card.objects.all()))

    return JsonResponse({'lists': list_json, 'cards': card_json})

def lists(request):
    list_json = json.loads(serialize('json', List.objects.all()))

    return JsonResponse({'lists': list_json})

def cards_in_list(request, pk):
    cards_in_list = get_object_or_404(CardsInList, pk=1)
    cards_in_list = json.loads(cards_in_list.json_data)
    return JsonResponse({'cards_in_list': cards_in_list})

@csrf_exempt
def edit_cards_in_list(request, pk):
    if request.method == 'POST':
        json_data = json.loads(json.dumps(QueryDict(request.body)))['cards_in_list']
        cards_in_list = get_object_or_404(CardsInList, pk=1)
        cards_in_list.json_data = json_data
        cards_in_list.save()
        return JsonResponse({'data': 'success'})
    raise Http404()
