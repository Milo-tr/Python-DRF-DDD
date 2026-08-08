from django.urls import path
from .views import ObtenerCrearTrabajador, ObtenerActualizarDestruirTrabajador

urlpatterns = [
    path('trabajador/', ObtenerCrearTrabajador.as_view(), name='trabajador-create'),
    path('trabajador/<uuid:pk>/', ObtenerActualizarDestruirTrabajador.as_view(), name='trabajador-create'),
]