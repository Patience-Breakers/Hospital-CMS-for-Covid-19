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


def bedavailibility(request):
    all_rooms_objects = Room.objects.all()
    list = []
    # for room_object in all_rooms_objects:

    context = {'list': list, 'all_rooms_objects': all_rooms_objects}
    return render(request, 'bedavailibility.html', context)


# def bedavailibility22(request):
#     all_floors = []
#     floornumbers = Room.objects.values('floor_no')
#     # print(floornumbers)
#     # for floor in floornumbers:
#     # if all_floors.__contains__
#     # print(floors)
#     context = {}
#     return render(request, 'bedavailibility.html', context)
