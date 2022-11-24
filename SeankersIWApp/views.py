from django.http import HttpResponse
from django.shortcuts import render
from .models import Sneaker
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
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

def checkout(request):
    return render(request, 'checkout.html')
