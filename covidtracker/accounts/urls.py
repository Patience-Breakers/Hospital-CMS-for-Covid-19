from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    # path("login", views.login, name='login'),
    path("dashboard/", views.dashboard, name='dashboard'),
    # path("addPatient", views.buttons, name='buttons'),
    path("search", views.search, name='search'),
    path("bedavailibility", views.bedavailibility, name='bedavailibility'),
    # path("bedavailibility22", views.bedavailibility22, name='bedavailibility22'),
    path('patients/<int:myid>/', views.patients, name='patientspages')
    # path("viewPatient", views.viewPatient, name='viewPatient'),
    # path("editPatient", views.editInfo, name='editPatient'),
    # path("searchRecovered", views.searchRecovered, name='searchRecovered'),
    # path("viewAll", views.viewAll, name='viewAll'),
    # path("searchAdmitted", views.searchAdmitted, name='searchAdmitted'),
    # path("searchVentilator", views.searchVentilator, name='searchVentilator'),
    # path("searchDecreased", views.searchDecreased, name='searchDecreased'),

]
