from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View

# Create your views here.

@login_required
def index(request):
    sneakers = Sneaker.objects.all()
    return render(request, 'index.html', {'sneakers': sneakers})

def products(request):
    sneakers = Sneaker.objects.all()
    return render(request, 'products.html', {'sneakers': sneakers})

def about(request):
    return render(request, 'about.html')

def faqs(request):
    return render(request, 'faqs.html')

def carrit(request):
    return render(request, 'shoppingcart.html')

def detalle(request, id):
    sneakers = Sneaker.objects.all()
    producto_selec = Sneaker.objects.get(id=id)
    return render(request, 'productdetail.html', {'producto_selec': producto_selec})


def checkout(request):
    return render(request, 'checkout.html')


class VRegistro(View):

    def get(self,request):
        form = UserCreationForm()
        return render(request, 'registro_prueba.html', {"form":form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        usuario=form.save()
        login(request, usuario)
        return redirect('index')


        
            





