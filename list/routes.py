from rest_framework.routers import DefaultRouter
from list.shopping import views as shopping_list_views
from list.views import User, ItemShopping, ItemSeries
from list.series import views as series_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()

router.register(r'user', User, basename='user')
router.register(r'item-shop', ItemShopping, basename='item-shop')
router.register(r'item-series', ItemSeries, basename='item-series')
router.register(r'shopping-list', shopping_list_views.List, basename='shopping-list')
#router.register(r'series-list', series_views.ListSerie, basename='series-list')
router.register(r'series-list', series_views.SerieInfoUser, basename='serie-user')
urlpatterns = router.urls