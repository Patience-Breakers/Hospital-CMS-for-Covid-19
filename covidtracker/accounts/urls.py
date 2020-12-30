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
    path("allpatients/", views.allpatients, name='allPatients'),

    # todo  forms have url mapping as 'name' not 'name/'

    path("search", views.search, name='search'),
    path("addpatient", views.addpatient, name='addpatient'),
    path("adddoctor", views.adddoctor, name='adddoctor'),


]
