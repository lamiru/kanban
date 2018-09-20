import json
from django.core.serializers import serialize
from django.http import Http404, JsonResponse, QueryDict
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from main.models import *


def items(request):
    list_dict = json.loads(serialize('json', List.objects.all()))
    list_json = {}
    for list in list_dict:
        list_json[list['pk']] = {
            'pk': list['pk'],
            'title': list['fields']['title'],
            'created_at': list['fields']['created_at'],
            'updated_at': list['fields']['updated_at'],
        }

    card_dict = json.loads(serialize('json', Card.objects.all()))
    card_json = {}
    for card in card_dict:
        card_json[card['pk']] = {
            'pk': card['pk'],
            'title': card['fields']['title'],
            'created_at': card['fields']['created_at'],
            'updated_at': card['fields']['updated_at'],
        }

    user_dict = json.loads(serialize('json', User.objects.all()))
    user_json = {}
    for user in user_dict:
        user_json[user['pk']] = {
            'pk': user['pk'],
            'username': user['fields']['username'],
            'first_name': user['fields']['first_name'],
            'last_name': user['fields']['last_name'],
        }

    return JsonResponse({'lists': list_json, 'cards': card_json, 'users': user_json})

def lists(request):
    list_dict = json.loads(serialize('json', List.objects.all()))
    list_json = {}
    for list in list_dict:
        list_json[list['pk']] = {
            'pk': list['pk'],
            'title': list['fields']['title'],
            'created_at': list['fields']['created_at'],
            'updated_at': list['fields']['updated_at'],
        }

    return JsonResponse(list_json)

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
