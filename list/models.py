from django.db import models
from polymorphic.models import PolymorphicModel

class User(models.Model):

    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

#items for diferent lists

class TypeOfItemList(models.TextChoices):
    SHOPPING = 'shopping', 'Shopping'
    SERIE = 'serie', 'Serie'
    MANGA = 'manga', 'Manga'
    BOOK = 'book', 'Book'
    #add types as new item list are needed

class Item(PolymorphicModel):

    name = models.CharField(max_length=50)

class ItemShopping(Item):
    type = models.CharField(
        max_length=10,
        default=TypeOfItemList.SHOPPING,
        choices={t.value: t.name
                 for t in { TypeOfItemList.SHOPPING}}
    )
    marketName = models.CharField(max_length=20, default="")

class ItemSerie(Item):
    type = models.CharField(
        max_length=10,
        default=TypeOfItemList.SERIE,
        choices={t.value: t.name
                 for t in { TypeOfItemList.SERIE}}
    )
    season = models.IntegerField(default=1)
    episode = models.IntegerField(default=1)
    website = models.CharField(max_length=80, default="")
    date = models.DateField(auto_now_add=True)