from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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

        if Contacto.objects.filter(telefono__iexact=telefono).exists():
            messages.error(request, "El teléfono ya está registrado.")

        elif Contacto.objects.filter(correo__iexact=correo).exists():
            messages.error(request, "El correo ya está registrado.")

        else:
            Contacto.objects.create(nombre = nombre, primerApellido = apellidoPaterno, segundoApellido = apellidoMaterno, alias = alias, relacion = relacion, telefono = telefono, correo = correo)
            return redirect("listar-contactos")
    
    relaciones = Relacion.objects.all()
    return render(request, "crear-contacto.html", {"relaciones": relaciones})

def editar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        contacto.nombre = request.POST["nombre"]
        contacto.primerApellido = request.POST["apellidoPaterno"]
        contacto.segundoApellido = request.POST["apellidoMaterno"]
        contacto.alias = request.POST["alias"]
        contacto.telefono = request.POST["telefono"]
        contacto.correo = request.POST["correo"]

        relacion_id = request.POST["relacion"]
        if relacion_id:
            contacto.relacion = Relacion.objects.get(id = relacion_id)

        if Contacto.objects.filter(telefono__iexact=contacto.telefono).exclude(id=contacto.id).exists():
            messages.error(request, "El teléfono ya está registrado.")

        elif Contacto.objects.filter(correo__iexact=contacto.correo).exclude(id=contacto.id).exists():
            messages.error(request, "El correo ya está registrado.")

        else:
            contacto.save()
            return redirect('listar-contactos')
        
    relaciones = Relacion.objects.all()
    return render(request, 'editar-contacto.html', {'contacto': contacto, 'relaciones': relaciones})

def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    contacto.delete()
    return redirect('listar-contactos')