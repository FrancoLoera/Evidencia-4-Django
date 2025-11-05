from django.shortcuts import render, redirect, get_object_or_404
from .models import Relacion, Contacto

# Create your views here.
def listar_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'listar-contactos.html', {'contactos': contactos})