from django.http import HttpResponse
from django.shortcuts import render
from .models import Sneaker

# Create your views here.

def index(request):
    return render(request, 'PaginaPrincipal.html')

def home(request):
    return render(request, 'index.html')