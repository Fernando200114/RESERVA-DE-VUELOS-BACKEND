from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Aerolinea, Avion, Vuelo, Pasajero, Reserva, Tripulacion



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]
        read_only_fields = ["id"]


class AerolineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aerolinea
        fields = ["id", "nombre", "pais", "codigo_iata", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class AvionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avion
        fields = ["id", "modelo", "capacidad", "matricula", "fabricante", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]


class VueloSerializer(serializers.ModelSerializer):
    aerolinea = AerolineaSerializer(read_only=True)
    aerolinea_id = serializers.PrimaryKeyRelatedField(
        queryset=Aerolinea.objects.all(),
        write_only=True,
        source="aerolinea"
    )

    avion = AvionSerializer(read_only=True)
    avion_id = serializers.PrimaryKeyRelatedField(
        queryset=Avion.objects.all(),
        write_only=True,
        source="avion",
        allow_null=True,
        required=False
    )

    class Meta:
        model = Vuelo
        fields = [
            "id", "numero_vuelo", "aerolinea", "aerolinea_id",
            "origen", "destino",
            "fecha_salida", "hora_salida", "fecha_llegada", "hora_llegada",
            "avion", "avion_id",
            "estado", "created_at", "updated_at"
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class PasajeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasajero
        fields = ["id", "nombres", "apellidos", "cedula", "correo", "telefono", "direccion"]
        read_only_fields = ["id"]


class ReservaSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    usuario_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        source="usuario"
    )

    vuelo = VueloSerializer(read_only=True)
    vuelo_id = serializers.PrimaryKeyRelatedField(
        queryset=Vuelo.objects.all(),
        write_only=True,
        source="vuelo"
    )

    pasajero = PasajeroSerializer(read_only=True)
    pasajero_id = serializers.PrimaryKeyRelatedField(
        queryset=Pasajero.objects.all(),
        write_only=True,
        source="pasajero"
    )

    class Meta:
        model = Reserva
        fields = [
            "id", "codigo_reserva", "usuario", "usuario_id",
            "vuelo", "vuelo_id", "pasajero", "pasajero_id",
            "fecha_reserva", "asiento", "estado"
        ]
        read_only_fields = ["id", "fecha_reserva"]


class TripulacionSerializer(serializers.ModelSerializer):
    avion = AvionSerializer(read_only=True)
    avion_id = serializers.PrimaryKeyRelatedField(
        queryset=Avion.objects.all(),
        write_only=True,
        source="avion",
        allow_null=True,
        required=False
    )

    class Meta:
        model = Tripulacion
        fields = ["id", "nombres", "apellidos", "rol", "avion", "avion_id"]
        read_only_fields = ["id"]
