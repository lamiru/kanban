from django.contrib import admin
from .models import *

# Register your models here.
class ListAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title',
        'created_at', 'updated_at',
    )

admin.site.register(List, ListAdmin)


class CardAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'contents',
        'created_at', 'updated_at',
    )

admin.site.register(Card, CardAdmin)


class CardsInListAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'json_data',
        'created_at', 'updated_at',
    )

admin.site.register(CardsInList, CardsInListAdmin)
