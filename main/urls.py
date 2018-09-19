from django.conf.urls import url
from .views import *

app_name = 'main'

urlpatterns = [
    url(r'^$', index, name='index'),
]
