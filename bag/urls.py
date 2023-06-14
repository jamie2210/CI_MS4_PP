from django.urls import path
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.view_bag, name='view_bag')
]
