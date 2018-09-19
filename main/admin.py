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
        'id', 'title', 'contents', 'list', 'order',
        'created_at', 'updated_at',
    )

admin.site.register(Card, CardAdmin)


class CardsInListAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'cards_in_list',
        'created_at', 'updated_at',
    )

admin.site.register(CardsInList, CardsInListAdmin)
