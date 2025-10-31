from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        descripcion = request.POST['descripcion']
        categoria_id = request.POST.get('categoria')

        categoria = Categoria.objects.get(id=categoria_id)

        Producto.objects.create(nombre=nombre, precio=precio, descripcion=descripcion, categoria=categoria)
        return redirect('listar')
    categorias = Categoria.objects.all()
    return render(request, 'crear.html', {'categorias': categorias})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.precio = request.POST['precio']
        producto.descripcion = request.POST['descripcion']
        
        categoria_id = request.POST['categoria']
        
        if categoria_id:
            producto.categoria = Categoria.objects.get(id=categoria_id)
        
        producto.save()
        return redirect('listar')
    categorias = Categoria.objects.all()
    return render(request, 'editar.html', {'producto': producto, 'categorias': categorias})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('listar')
