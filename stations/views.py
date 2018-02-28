from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render

from .models import Station, StationUrl
from .forms import StationForm

def index(request):
    context = {
        "stations": Station.objects.all()
    }
    return render(request, 'stations/index.html', context)

def stations_json(request):
    stations = [{
        "name": s.name,
        "description": s.description,
        "urls": [s_url.url for s_url in s.urls.all()],
    } for s in Station.objects.all()]
    return JsonResponse(stations, safe=False)

def add_station(request):
    if request.method == "POST":
        raise Http404("Not implemented")
    return render(request, 'stations/addstation.html')