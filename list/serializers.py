from list.models import User, ItemShopping, ItemSerie
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = "__all__"

class ItemShoppingSerializer(serializers.ModelSerializer):

    class Meta:

        model = ItemShopping
        fields = ['id', 'name', 'type', 'marketName']

class ItemSerieSerializer(serializers.ModelSerializer):

    class Meta:

        model = ItemSerie
        fields = ['id', 'name', 'type', 'season', 'episode', 'website', 'date']