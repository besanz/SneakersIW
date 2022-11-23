from django.http import HttpResponse
from django.shortcuts import render
from .models import Sneaker

# Create your views here.

def index(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def faqs(request):
    return render(request, 'faqs.html')

def carrit(request):
    return render(request, 'shoppingcart.html')

def pDetail(request):
    return render(request, 'productdetail.html')