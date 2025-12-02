from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_usuarios, name='listar'),
    path('crear/', views.crear_usuario, name='crear'),
    path('actualizar/<int:id>/', views.actualizar_usuario, name='actualizar'),
    path('eliminar/<int:id>/', views.eliminar_usuario, name='eliminar'),
]