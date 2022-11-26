from django.urls import path
from . import views
from .views import VRegistro

urlpatterns = [
    path('', views.index, name='index'),
    path('Products', views.products, name='products'),
    path('About', views.about, name='about'),
    path('Faqs', views.faqs, name='faqs'),
    path('Carrito', views.carrit, name='carrit'),
    path('Detalles_de_producto/<int:id>', views.detalle, name='productdetail'),
    path('Checkout', views.checkout, name='checkout'),
    path('Registro', VRegistro.as_view(), name='Autenticacion')
    

]