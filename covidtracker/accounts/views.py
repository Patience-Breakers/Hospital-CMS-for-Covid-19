# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Patient, Room
import collections


def index(request):
    return render(request, 'mainPage/index.html')

# todo ----------part of dashboard starts here----------------------------------


def age_list_calc_for_dashboard_pie(all_patients):
    all_age = []
    for patient in all_patients:
        all_age.append(patient.age)
    tally_age = collections.Counter()
    for i in all_age:
        tally_age[i] = tally_age[i]+1
    return tally_age


def temp_list_calc_for_dashboard_pie(all_patients):
    all_temp = []
    for patient in all_patients:
        all_temp.append(patient.temperature)
    tally_temperature = collections.Counter()
    for i in all_temp:
        tally_temperature[i] = tally_temperature[i]+1
    return tally_temperature


def dashboard(request):
    all_patients = Patient.objects.all()
    tally_age = age_list_calc_for_dashboard_pie(all_patients)
    tally_temperature = temp_list_calc_for_dashboard_pie(all_patients)

    list_keys_age = list(tally_age)
    list_values_age = list(tally_age.values())

    list_keys_temp = list(tally_temperature)
    list_values_temp = list(tally_temperature.values())

    context = {'all_patients': all_patients,
               'list_keys_age': list_keys_age, 'list_values_age': list_values_age, 'list_keys_temp': list_keys_temp, 'list_values_temp': list_values_temp}
    return render(request, 'dashboard.html', context)
# todo ----------part of dashboard ends here----------------------------------


def search(request):
    if request.method == 'POST':
        query = request.POST.get('name', '')
        all_search_patients_acc_to_name = Patient.objects.filter(
            name__icontains=query)
        context = {
            'all_search_patients_acc_to_name': all_search_patients_acc_to_name, 'query': query}
        return render(request, 'result_of_search.html', context)

    return render(request, 'result_of_search.html')


def bedavailability(request):
    all_rooms_objects = Room.objects.all()
    max_rooms_on_floor = 6

    context = {'list': list, 'all_rooms_objects': all_rooms_objects,
               'max_rooms_on_floor': max_rooms_on_floor}
    return render(request, 'bedavailability.html', context)


def patients(request, myid):
    patient = Patient.objects.filter(patient_id=myid)
    return render(request, 'patient.html', {'patient': patient[0]})


def allpatients(request):
    return render(request, 'allpatients.html')
