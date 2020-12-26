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
    if request.method == 'POST':
        query = request.POST.get('name', '')
        all_search_patients_acc_to_name = Patient.objects.filter(
            name__icontains=query)
        context = {
            'all_search_patients_acc_to_name': all_search_patients_acc_to_name, 'query': query}
        return render(request, 'search.html', context)

    return render(request, 'search.html')


def bedavailibility(request):
    all_rooms_objects = Room.objects.all()
    max_rooms_on_floor = 6

    context = {'list': list, 'all_rooms_objects': all_rooms_objects,
               'max_rooms_on_floor': max_rooms_on_floor}
    return render(request, 'bedavailibility.html', context)


def patients(request, myid):
    patient = Patient.objects.filter(patient_id=myid)
    return render(request, 'patient.html', {'patient': patient[0]})
