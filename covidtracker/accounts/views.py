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


# def bedavailibility22(request):
#     floors_rooms = Room.objects.all()
#     # todo maximum rooms per floor\\
#     counter = 0
#     floor = 1
#     list = []
#     for room in floors_rooms:
#         list.append(room)
#         if counter % 6 == 0:
#             floor = floor + 1

#     print(list)

#     max_rooms = 6
#     max_floors = range(1, 3)
#     context = {'list': list,
#                'max_rooms': max_rooms, 'max_floors': max_floors}
#     return render(request, 'bedavailibility.html', context)


def bedavailibility22(request):
    finallist = []
    all_floors = []
    Allbeds = Room.objects.all()
    floornumbers = Room.objects.values('floor_no')
    print(floornumbers)
    print(type(floornumbers))
    for bed in Allbeds:
        if bed.floor_no in all_floors :
            continue
        else :
            all_floors.append(bed.floor_no)
    print(all_floors)
    for floor in all_floors :
        beds = Room.objects.filter(floor_no=floor)
        finallist.append(beds)

       

    context = {'finallist':finallist}
    return render(request, 'bedavailibility.html', context)
