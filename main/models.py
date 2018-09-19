from django.db import models


class List(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Card(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    contents = models.TextField(blank=True, null=True, db_index=True)
    list = models.ForeignKey(List, db_index=True, related_name='list_cards')
    order = models.PositiveIntegerField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
