from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addstation', views.add_station, name='add_station'),
    path('apiv1/stations', views.stations_json, name='stations_json'),
]