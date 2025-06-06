from django.shortcuts import render
from .models import Personal_Data
# Create your views here.

def index(request):
    doctors = Personal_Data.objects.all()
    return render(request, 'index.html', context={'doctors' : doctors})