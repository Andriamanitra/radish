from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Station, StationUrl
from .forms import StationForm, StationUrlForm


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
        form = StationForm(request.POST)
        if form.is_valid() and form.url_is_good():
            if len(Station.objects.all()) >= 100:
                context = {
                    "title": "Database full!",
                    "content": "Your submission was not added because \
                    there are already too many radio stations stored \
                    in the database."
                }
                return render(request, 'stations/generic.html', context)
            form.store()
            context = {
                "title": "Station added!",
                "content": "{} was added to the database successfully."
                .format(form.cleaned_data["name"])
            }
            return render(request, 'stations/generic.html', context)
        else:
            context = {
                "title": "Invalid form!",
                "content": "Your submission was not added because the \
                form contained invalid data."
            }
            return render(request, 'stations/generic.html', context)
    else:
        form = StationForm()
    return render(request, 'stations/addstation.html', {'form': form})


def add_url(request, station_id):
    if request.method == "POST":
        form = StationUrlForm(request.POST)
        print(form)
        if form.is_valid():
            s_url = form.save(commit=False)
            s_url.station = get_object_or_404(Station, id=station_id)
            s_url.save()
            context = {
                "title": "Url added!",
                "content": "{} was added as a new url for {}"
                .format(s_url.url, s_url.station)
            }
            return render(request, 'stations/generic.html', context)
        else:
            context = {
                "title": "Invalid form!",
                "content": "Your submission was not added because the \
                form contained invalid data."
            }
            return render(request, 'stations/generic.html', context)
    else:
        station = Station.objects.get(id=station_id)
        context = {
            "station": station,
            "form": StationUrlForm()
        }
        return render(request, 'stations/addurl.html', context)
