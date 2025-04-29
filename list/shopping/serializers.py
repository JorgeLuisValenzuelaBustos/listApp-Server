from rest_framework import serializers
from list.shopping import models
from list.serializers import UserSerializer, ItemShoppingSerializer
from list.models import User, ItemShopping

'''class ListSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    item = ItemShoppingSerializer(source = "item_set", many=True)
    
    class Meta:

        model = models.List
        fields = [
            'id',
            'listName',
            'item',
            'user',
            'date'
        ]
'''

class ListWriteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    item = serializers.PrimaryKeyRelatedField(queryset=ItemShopping.objects.all(), many=True)

    class Meta:
        model = models.List
        fields = ['id', 'item', 'user', 'date']

class ListReadSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    item = ItemShoppingSerializer(many=True)

    class Meta:
        model = models.List
        fields = ['id', 'item', 'user', 'date']