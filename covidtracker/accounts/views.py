# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import Patient
# from accounts.models import Patient


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def search(request):
    return render(request, 'searchresult.html')


def bedavailibility(request):
    return render(request, 'bedavailibility.html')
