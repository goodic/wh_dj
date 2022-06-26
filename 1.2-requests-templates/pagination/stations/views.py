from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
import csv
import pagination.settings


with open(pagination.settings.BUS_STATION_CSV, encoding="UTF-8") as csvfile:
    CONTENT = list(csv.DictReader(csvfile))

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    bus_stations = paginator.get_page(page_number)
    print(bus_stations)
    context = {
         'bus_stations': bus_stations,
         'page': bus_stations,
    }
    return render(request, 'stations/index.html', context)

