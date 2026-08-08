from django.urls import path
from .views import ObtenerCrearUsuario, ObtenerActualizarDestruirUsuario

urlpatterns = [
    path('usuario/', ObtenerCrearUsuario.as_view(), name='usuario-create'),
    path('usuario/<uuid:pk>/', ObtenerActualizarDestruirUsuario.as_view(), name='usuario-create'),
]