from django.urls import path
from . import views

urlpatterns = [

   # path('', views.index, name='index'),
    path('', views.index, name='prueba'),
    path('Home', views.home, name='home')
    

]