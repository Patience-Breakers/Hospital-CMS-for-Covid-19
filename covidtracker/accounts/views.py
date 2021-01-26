# Create your views here.
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Patient, Room, Doctor
from .forms import PatientForm, DoctorForm
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


def bed_list_calc_for_dashboard_pie():
    all_rooms = Room.objects.all()
    total_no_of_rooms = all_rooms.count()
    occupied_rooms = 0
    for i in all_rooms:
        if i.occupied == True:
            occupied_rooms += 1

    return occupied_rooms, total_no_of_rooms


def dashboard(request):
    all_patients = Patient.objects.all()
    tally_age = age_list_calc_for_dashboard_pie(all_patients)
    tally_temperature = temp_list_calc_for_dashboard_pie(all_patients)
    no_of_occupied_beds, total_no_of_beds = bed_list_calc_for_dashboard_pie()
    non_occupied_no_of_beds = total_no_of_beds-no_of_occupied_beds
    list_keys_age = list(tally_age)
    list_values_age = list(tally_age.values())
    list_keys_temp = list(tally_temperature)
    list_values_temp = list(tally_temperature.values())

    context = {
        'all_patients': all_patients,
        'list_keys_age': list_keys_age,
        'list_values_age': list_values_age,
        'list_keys_temp': list_keys_temp,
        'list_values_temp': list_values_temp,
        'no_of_occupied_beds': no_of_occupied_beds,
        'non_occupied_no_of_beds': non_occupied_no_of_beds,
    }
    return render(request, 'dashboard.html', context)
# todo ----------part of dashboard ends here----------------------------------


def search(request):
    if request.method == 'POST':
        query = request.POST.get('name', '')
        all_search_patients_acc_to_name = Patient.objects.filter(
            name__icontains=query)
        context = {
            'all_search_patients_acc_to_name': all_search_patients_acc_to_name,
            'query': query
        }
        return render(request, 'result_of_search.html', context)

    return render(request, 'result_of_search.html')


def bedavailability(request):
    all_rooms_objects = Room.objects.all()
    max_rooms_on_floor = 6

    context = {
        'list': list,
        'all_rooms_objects': all_rooms_objects,
        'max_rooms_on_floor': max_rooms_on_floor,
    }
    return render(request, 'bedavailability.html', context)


def doctoravailability(request):
    all_doctor_objects = Doctor.objects.all()
    context = {
        'all_doctors': all_doctor_objects
    }
    return render(request, 'doctoravailability.html', context)


def patients(request, myid):
    patient = Patient.objects.filter(patient_id=myid)
    return render(request, 'patient.html', {'patient': patient[0]})


def deleteDoctor(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    doctor_id = doctor.doctor_id
    try:
        patient = Patient.objects.get(doctor=doctor_id)
        room_id = patient.room_no_and_bed_no
        room = Room.objects.get(room_no=room_id)
        room.occupied = False
        room.ventilator = False
        room.save()
        doctor.delete()
    except:
        doctor.delete()

    return redirect('/doctoravailability/')


def deletePatient(request, myid):
    patient = Patient.objects.get(patient_id=myid)
    doctor_id = patient.doctor.pk
    doctor = Doctor.objects.get(pk=doctor_id)
    room_id = patient.room_no_and_bed_no
    room = Room.objects.get(room_no=room_id)
    patient.delete()
    room.occupied = False
    room.ventilator = False
    doctor.occupied = False
    doctor.save()
    room.save()
    return redirect('/allpatients')


def doctors(request, myid):
    doctor = Doctor.objects.filter(doctor_id=myid)
    return render(request, 'doctor.html', {'doctor': doctor[0]})


def allpatients(request):
    all_patients_query_set = Patient.objects.all()
    context = {
        'all_patients_query_set': all_patients_query_set
    }
    return render(request, 'allpatients.html', context)


def adddoctor(request):
    # if we get POST method, we will use this
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/doctoravailability/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = DoctorForm()
        return render(request, 'adddoctor.html', {'form': form})


def addpatient(request):
    # if we get POST method, we will use this
    if request.method == 'POST':
        form = PatientForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            room_no = request.POST.get('room_no_and_bed_no')
            ventilator = request.POST.get('ventilator')
            doctor_no = request.POST.get('doctor')
            room = Room.objects.get(pk=room_no)
            room.occupied = True
            if ventilator == 'yes':
                room.ventilator = True
            room.save()
            # todo docotor avialable changed
            # doctor = Room.objects.get(pk=3)
            doctor = Doctor.objects.get(pk=doctor_no)
            doctor.occupied = True
            doctor.save()
            return HttpResponseRedirect('/allpatients/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PatientForm()
        return render(request, 'add_patient.html', {'form': form})


# todo to go to the patient from bed availability
def bedforpatient(request, bedno):
    print(bedno)
    print(type(bedno))
    patients = Patient.objects.filter(room_no_and_bed_no=bedno)
    try:
        empty = False
        context = {
            'patients': patients,
            'first_patient': patients[0],
            'empty': empty,
        }
    except:
        empty = True
        context = {
            'patients': patients,
            'empty': empty,

        }
    return render(request, 'patientsfrombedavailability.html', context)
