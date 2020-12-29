from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path("dashboard/", views.dashboard, name='dashboard'),
    path("search", views.search, name='search'),
    path("bedavailability/", views.bedavailability, name='bedavailability'),
    path('patients/<int:myid>/', views.patients, name='patientspages'),
    path("allpatients/", views.allpatients, name='allPatients'),
    path("addpatient", views.addpatient, name='addpatient'),
    # path("addPatient", views.buttons, name='buttons'),
    # path("bedavailibility22", views.bedavailibility22, name='bedavailibility22'),
    # path("viewPatient", views.viewPatient, name='viewPatient'),
    # path("searchRecovered", views.searchRecovered, name='searchRecovered'),
    # path("viewAll", views.viewAll, name='viewAll'),
    # path("searchAdmitted", views.searchAdmitted, name='searchAdmitted'),
    # path("searchVentilator", views.searchVentilator, name='searchVentilator'),
    # path("searchDecreased", views.searchDecreased, name='searchDecreased'),

]
