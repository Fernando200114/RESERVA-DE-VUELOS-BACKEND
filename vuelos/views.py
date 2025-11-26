from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Aerolinea, Avion, Vuelo, Pasajero,Reserva,Tripulacion
from .serializers import AerolineaSerializer, AvionSerializer, VueloSerializer, PasajeroSerializer,ReservaSerializer,TripulacionSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_response = {
            "errors": response.data,
            "status_code": response.status_code
        }
        return Response(custom_response, status=response.status_code)

    return Response({
        "errors": str(exc),
        "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



from rest_framework.permissions import AllowAny

class AerolineaViewSet(viewsets.ModelViewSet):
    queryset = Aerolinea.objects.all()
    serializer_class = AerolineaSerializer
    
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nombre", "codigo_iata"]
    ordering_fields = ["nombre"]


class AvionViewSet(viewsets.ModelViewSet):
    queryset = Avion.objects.all()
    serializer_class = AvionSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["matricula", "modelo"]
    ordering_fields = ["matricula", "capacidad"]


class VueloViewSet(viewsets.ModelViewSet):
    queryset = Vuelo.objects.select_related("aerolinea", "avion").all()
    serializer_class = VueloSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["aerolinea", "origen", "destino", "fecha_salida", "estado"]
    search_fields = ["numero_vuelo", "origen", "destino"]
    ordering_fields = ["fecha_salida", "numero_vuelo"]


class PasajeroViewSet(viewsets.ModelViewSet):
    queryset = Pasajero.objects.all()
    serializer_class = PasajeroSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["nombres", "apellidos", "cedula"]



class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.select_related("usuario", "vuelo", "pasajero").all()
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["usuario", "vuelo", "pasajero", "estado"]
    search_fields = ["codigo_reserva", "usuario__username", "pasajero__nombres"]
    ordering_fields = ["fecha_reserva", "codigo_reserva"]


class TripulacionViewSet(viewsets.ModelViewSet):
    queryset = Tripulacion.objects.select_related("avion").all()
    serializer_class = TripulacionSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["nombres", "apellidos", "rol", "avion__matricula"]
    ordering_fields = ["apellidos", "nombres"]