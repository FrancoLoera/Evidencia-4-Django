from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_contactos, name='listar-contactos'),
    path('crear-contacto/', views.crear_contacto, name='crear-contacto'),
    path('editar-contacto/<int:id>/', views.editar_contacto, name='editar-contacto'),
    path('eliminar-contacto/<int:id>/', views.eliminar_contacto, name='eliminar-contacto'),
]