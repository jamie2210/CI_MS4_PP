from django.urls import path
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.view_favourites, name='view_favourites'),
    path('add_favourites/<item_id>', views.add_to_favourites,
         name='add_to_favourites'),
    path('remove_from_favourites_in_favourites/<item_id>/',
         views.remove_from_favourites_in_favourites,
         name='remove_from_favourites_in_favourites'),
    path('remove_from_favourites_in_products_detail/<item_id>/',
         views.remove_from_favourites_in_products_detail,
         name='remove_from_favourites_in_products_detail'),
]
