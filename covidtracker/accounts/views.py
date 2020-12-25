# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Patient, Room
# from accounts.models import Patient


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def search(request):
    return render(request, 'searchresult.html')


def bedavailibility22(request):
    floors_rooms = Room.objects.all()
    # todo maximum rooms per floor\\
    counter = 0
    floor = 1
    list = []
    for room in floors_rooms:
        list.append(room)
        if counter % 6 == 0:
            floor = floor + 1

    print(list)

    max_rooms = 6
    max_floors = range(1, 3)
    context = {'list': list,
               'max_rooms': max_rooms, 'max_floors': max_floors}
    return render(request, 'bedavailibility.html', context)


def bedavailibility(request):
    all_floors = []
    floornumbers = Room.objects.values('floor_no')
    # print(floornumbers)
    # for floor in floornumbers:
        # if all_floors.__contains__
    # print(floors)
    context = {}
    return render(request, 'bedavailibility.html', context)
