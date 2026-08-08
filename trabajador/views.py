from django.shortcuts import render
from rest_framework import generics
from .models import Trabajador
from .serializers import TrabajadorSerializer
from drf_spectacular.utils import extend_schema, OpenApiExample

class ObtenerCrearTrabajador(generics.ListCreateAPIView):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer

    @extend_schema(
        examples=[
            OpenApiExample(
                'Ejemplo de creación',
                value={
                    'rut': '12345678-9',
                    'nombre': 'Ana',
                    'segundo_nombre': 'María',
                    'apellido_paterno': 'Pérez',
                    'apellido_materno': 'Soto',
                    'correo': 'ana.perez@mail.com',
                    'telefono': '+56912345678',
                },
            )
        ]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class ObtenerActualizarDestruirTrabajador(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trabajador.objects.all()
    serializer_class = TrabajadorSerializer