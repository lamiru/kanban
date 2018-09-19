import json
from django.core.serializers import serialize
from django.http import Http404, JsonResponse
from django.shortcuts import render
from main.models import *


# Create your views here.
def items(request):
    list_json = json.loads(serialize('json', List.objects.all()))
    card_json = json.loads(serialize('json', Card.objects.all()))

    return JsonResponse({'list': list_json, 'card': card_json})
