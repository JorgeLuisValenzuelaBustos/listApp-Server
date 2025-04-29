from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from list.shopping import models, serializers
from list.serializers import UserSerializer
from list.models import User, ItemShopping
from rest_framework.response import Response
from rest_framework import status
import json

class List(ModelViewSet):

    queryset = models.List.objects.all()
    serializer_class = serializers.ListReadSerializer

    @action(detail=False, methods=['get'])
    def list_user(self, request):
        email = request.query_params.get('email')  # Use query parameters for GET requests
        if not email:
            return Response({'error': 'Email is required.'}, status=400)

        listUser = models.List.objects.filter(user__email=email).order_by('-id')
        serializer = serializers.ListReadSerializer(listUser, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        user = body['user']
        email = body['email']
        items = body['items']
        if not User.objects.filter(email = email).count():
            data = {'name': user, 'email': email}
            serializer = UserSerializer (data = data)

            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(email = email).first()
        itemList = []
        for item in items:
            item_instance = ItemShopping.objects.filter(name = item).first()
            if item_instance:
                itemList.append(item_instance.id)
        listData = {'item': itemList, 'user': user.id}
        serializer = serializers.ListWriteSerializer(data = listData)
        if serializer.is_valid():
            listName = serializer.save()

            return Response(serializers.ListWriteSerializer(listName).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        items = body['item']
        instruction = body['instruction']
        list_instance = models.List.objects.filter(id=pk).first()
        if instruction == "add":
            for item in items:
                item_instance = ItemShopping.objects.filter(name = item).first()
                list_instance.item.add(item_instance.id)
            return Response(status=status.HTTP_200_OK)
        elif instruction == "remove":
            item_instance = ItemShopping.objects.filter(name = items).first()
            if item_instance:
                list_instance.item.remove(item_instance)
            return Response(status=status.HTTP_200_OK)
            
