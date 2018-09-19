from django.conf.urls import url
from .views import *

app_name = 'api'

urlpatterns = [
    url(r'^items$', items, name='items'),
    url(r'^lists$', lists, name='lists'),
    url(r'^cards_in_list/(?P<pk>\d+)$', cards_in_list, name='cards_in_list'),
]
