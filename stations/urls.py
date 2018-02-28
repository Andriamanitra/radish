from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addstation', views.add_station, name='add-station'),
    path(r'addurl/<int:station_id>/', views.add_url, name="add-url"),
    path('apiv1/stations', views.stations_json, name='stations-json'),
]
