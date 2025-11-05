from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productos, name='listar'),
    path('crear/', views.crear_producto, name='crear'),
    path('editar/<int:id>/', views.editar_producto, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar'),
    path('listar-categorias/', views.listar_categorias, name='listar-categorias'),
    path('crear-categoria/', views.crear_categoria, name="crear-categoria"),
    path('editar-categoria/<int:id>/', views.editar_categoria, name="editar-categoria"),
    path('eliminar-categoria/<int:id>/', views.eliminar_categoria, name="eliminar-categoria"),
]
