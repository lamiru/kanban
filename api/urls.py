from django.conf.urls import url
from .views import *

app_name = 'api'

urlpatterns = [
    url(r'^items$', items, name='items'),
]
