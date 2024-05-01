from django.db import models


class Item(models.Model):
    id_item = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    quantidade = models.IntegerField()
