from rest_framework import serializers
from list.series import models
from list.serializers import UserSerializer, ItemSerieSerializer
from list.models import User, ItemSerie

class SerieInfoUserWriteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    serie = serializers.PrimaryKeyRelatedField(queryset=ItemSerie.objects.all())

    class Meta:
        model = models.SerieInfoUser
        fields = ['id', 'serie', 'season', 'episode', 'user', 'updated_at']

class SerieInfoUserReadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    serie = ItemSerieSerializer(read_only=True)

    class Meta:
        model = models.SerieInfoUser
        fields = ['id', 'serie', 'season', 'episode', 'user', 'updated_at']