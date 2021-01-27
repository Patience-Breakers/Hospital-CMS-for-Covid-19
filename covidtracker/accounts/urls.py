from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("bedavailability/", views.bedavailability, name='bedavailability'),
    path("doctoravailability/", views.doctoravailability,
         name='doctoravailability'),
    path('patients/<int:myid>/', views.patients, name='patientspages'),
    path('doctors/<int:myid>/', views.doctors, name='doctorspages'),
    path("allpatients/", views.allpatients, name='allPatients'),
    # todo Delete the patient, Doctor
    path('deletePatient/<int:myid>/', views.deletePatient, name='deletePatient'),
    path('deleteDoctor/<int:pk>/', views.deleteDoctor, name='deleteDoctor'),
    path('bed-for-patient/<int:bedno>/',
         views.bedforpatient, name='bedforpatient'),
    # todo  forms have url mapping as 'name' not 'name/'

    path("search", views.search, name='search'),
    path("addpatient", views.addpatient, name='addpatient'),
    path("adddoctor", views.adddoctor, name='adddoctor'),
    path("edititems", views.edititems, name="edititems"),
]
