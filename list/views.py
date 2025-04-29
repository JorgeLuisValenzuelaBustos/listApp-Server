from rest_framework.viewsets import ModelViewSet
from list.serializers import UserSerializer, ItemShoppingSerializer, ItemSerieSerializer
from list.models import ItemShopping
from list.models import User as Users
from list.models import ItemSerie

class User(ModelViewSet):

    queryset = Users.objects.all()
    serializer_class = UserSerializer

class ItemShopping(ModelViewSet):

    queryset = ItemShopping.objects.all()
    serializer_class = ItemShoppingSerializer

class ItemSeries(ModelViewSet):

    queryset = ItemSerie.objects.all()
    serializer_class = ItemSerieSerializer