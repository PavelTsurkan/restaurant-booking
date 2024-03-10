from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'restauraunt_managment_app/index.html')


def add_booking(request):
    places = Place.objects.all()

    if request.method == "POST":
        print(request.POST)
    else:
        print(request.GET)

    return render(request, 'restauraunt_managment_app/add_booking.html', context={"places": places})