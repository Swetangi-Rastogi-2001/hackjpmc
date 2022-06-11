from django.shortcuts import render
from . import forms 
from . import models

# Create your views here.

def Home(request):
    return render(request, 'home.html')


def profiling_attempt(request):
    return render(request, 'Profiling.html')