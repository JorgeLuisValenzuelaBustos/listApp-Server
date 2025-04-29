from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from list.series import models, serializers
from list.serializers import UserSerializer
from list.models import User, ItemSerie
from rest_framework.response import Response
from rest_framework import status
import json

class SerieInfoUser(ModelViewSet):

    queryset = models.SerieInfoUser.objects.all()
    serializer_class = serializers.SerieInfoUserReadSerializer

    @action(detail=False, methods=['get'])
    def list_user(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({'error': 'Email is required.'}, status=400)
        listUser = models.SerieInfoUser.objects.filter(user__email=email).order_by('-id')
        serializer = serializers.SerieInfoUserReadSerializer(listUser, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        user = body['user']
        email = body['email']
        serieName = body['name']
        seriSeason = body['season']
        serieEpisode = body['episode']


        if not User.objects.filter(email=email).count():
            data = {'name': user, 'email': email}
            serializer = UserSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        print(serieName)
        user = User.objects.filter(email=email).first()
        serie = ItemSerie.objects.filter(name=serieName).first()
        if not models.SerieInfoUser.objects.filter(serie=serie.id).count():
            data = {'serie': serie.id, 'season': seriSeason, 'episode': serieEpisode, 'user': user.id}
            serializer = serializers.SerieInfoUserWriteSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
        return Response(status=status.HTTP_201_CREATED)
    

    def update(self, request, pk=None):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        id = body['id']
        season = body['season']
        episode = body['episode']
        serie = models.SerieInfoUser.objects.filter(id=id).first()
        serie.season = season
        serie.episode = episode
        serie.save()
        return Response(status=status.HTTP_200_OK)
        

"""class ListSerie(ModelViewSet):
    
        queryset = models.ListSeries.objects.all()
        serializer_class = serializers.ListSeriesReadSerializer
    
        @action(detail=False, methods=['get'])
        def list_user(self, request):
            email = request.query_params.get('email')  # Use query parameters for GET requests
            if not email:
                return Response({'error': 'Email is required.'}, status=400)
    
            listUser = models.ListSeries.objects.filter(user__email=email).order_by('-id')
            serializer = serializers.ListSeriesReadSerializer(listUser, many=True)
    
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        def create(self, request):
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            user = body['user']
            email = body['email']
            items = body['item']
            
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
                if not models.SerieInfoUser.objects.filter(serie = item.serie_id).count():
                    data = {'serie': item_instance.id, 'season': item.season, 'episode': item.episode}
                    serializer = serializers.SerieInfoUserSerializer(data = data)
    
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                item_instance = models.SerieInfoUser.objects.filter(serie = item.serie_id).first()
                itemList.append(item_instance.id)
            listData = {'item': itemList, 'user': user.id}
            serializer = serializers.ListSeriesWriteSerializer(data = listData)
            if serializer.is_valid():
                listName = serializer.save()
    
                return Response(serializers.ListSeriesWriteSerializer(listName).data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""