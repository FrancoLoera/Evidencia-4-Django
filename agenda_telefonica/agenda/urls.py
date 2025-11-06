from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_contactos, name='listar-contactos'),
    path('crear-contacto/', views.crear_contacto, name='crear-contacto'),
]