from django.conf.urls import url
from .views import *

app_name = 'api'

urlpatterns = [
    url(r'^items$', items, name='items'),
    url(r'^lists$', lists, name='lists'),
    url(r'^list_card_order/(?P<pk>\d+)$', list_card_order, name='list_card_order'),
    url(r'^list_card_order/(?P<pk>\d+)/edit$', edit_list_card_order, name='edit_list_card_order'),
]
