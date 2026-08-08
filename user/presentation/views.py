from rest_framework import generics
from user.application.use_cases.crear_usuario_con_trabajador import CrearUsuarioConTrabajador
from .serializers import UserSerializer, Usuario
from drf_spectacular.utils import extend_schema, OpenApiExample

class ObtenerCrearUsuario(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

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

class ObtenerActualizarDestruirUsuario(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer