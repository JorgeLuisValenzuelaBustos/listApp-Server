from django.db import models
from django.db.models.deletion import CASCADE
from list.models import User, ItemSerie


class SerieInfoUser(models.Model):
    serie = models.ForeignKey(ItemSerie, on_delete=CASCADE)
    season = models.IntegerField(default=1)
    episode = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    
