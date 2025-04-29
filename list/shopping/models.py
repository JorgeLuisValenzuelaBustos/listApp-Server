from django.db import models
from django.db.models.deletion import CASCADE
from list.models import User, ItemShopping


class List(models.Model):

    user = models.ForeignKey(User, on_delete=CASCADE)
    item = models.ManyToManyField(ItemShopping, related_name="lists")
    date = models.DateField(auto_now_add=True)
