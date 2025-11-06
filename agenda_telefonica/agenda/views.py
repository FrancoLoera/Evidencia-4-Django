from django.shortcuts import render, redirect, get_object_or_404
from .models import Relacion, Contacto

# Create your views here.
def listar_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'listar-contactos.html', {'contactos': contactos})

def crear_contacto(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        apellidoPaterno = request.POST["apellidoPaterno"]
        apellidoMaterno = request.POST.get("apellidoMaterno", "")
        alias = request.POST.get("alias", "")
        
        relacion_id = request.POST.get("relacion")
        relacion = Relacion.objects.get(id = relacion_id)
        
        telefono = request.POST["telefono"]
        correo = request.POST.get("correo", "")
        
        Contacto.objects.create(nombre = nombre, apellidoPaterno = apellidoPaterno, apellidoMaterno = apellidoMaterno, alias = alias, relacion = relacion, telefono = telefono, correo = correo)
        return redirect("listar-contactos")
    
    relaciones = Relacion.objects.all()
    return render(request, "crear-contacto.html", {"relaciones": relaciones})