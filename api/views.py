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

def list_card_order(request, pk):
    list_card_order = get_object_or_404(ListCardOrder, pk=1)
    cards_in_list = json.loads(list_card_order.cards_in_list)
    list_order = json.loads(list_card_order.list_order)

    return JsonResponse({'cards_in_list': cards_in_list, 'list_order': list_order})

@csrf_exempt
def edit_list_card_order(request, pk):
    if request.method == 'POST':
        list_card_order = get_object_or_404(ListCardOrder, pk=1)
        list_card_order.cards_in_list = json.loads(json.dumps(QueryDict(request.body)))['cards_in_list']
        list_card_order.list_order = json.loads(json.dumps(QueryDict(request.body)))['list_order']
        print(request.body)
        list_card_order.save()
        return JsonResponse({'data': 'success'})
    raise Http404()
