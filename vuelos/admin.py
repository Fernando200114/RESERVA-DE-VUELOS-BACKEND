from django.contrib import admin
from django.contrib.auth.models import User  
from .models import Aerolinea, Avion, Vuelo, Pasajero, Reserva, Tripulacion


@admin.register(Aerolinea)
class AerolineaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "codigo_iata", "pais", "created_at")
    search_fields = ("nombre", "codigo_iata")
    list_filter = ("pais",)

@admin.register(Avion)
class AvionAdmin(admin.ModelAdmin):
    list_display = ("matricula", "modelo", "capacidad", "fabricante")
    search_fields = ("matricula", "modelo")
    list_filter = ("fabricante",)

@admin.register(Vuelo)
class VueloAdmin(admin.ModelAdmin):
    list_display = ("numero_vuelo", "aerolinea", "origen", "destino", "fecha_salida", "hora_salida", "estado")
    search_fields = ("numero_vuelo", "origen", "destino")
    list_filter = ("estado", "aerolinea")

@admin.register(Pasajero)
class PasajeroAdmin(admin.ModelAdmin):
    list_display = ("nombres", "apellidos", "cedula", "correo", "telefono")
    search_fields = ("nombres", "apellidos", "cedula", "correo")


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("codigo_reserva", "usuario", "pasajero", "vuelo", "fecha_reserva", "estado", "asiento")
    search_fields = ("codigo_reserva", "usuario__username", "pasajero__nombres", "vuelo__numero_vuelo")
    list_filter = ("estado", "vuelo__aerolinea")

@admin.register(Tripulacion)
class TripulacionAdmin(admin.ModelAdmin):
    list_display = ("nombres", "apellidos", "rol", "avion")
    search_fields = ("nombres", "apellidos", "rol", "avion__matricula")
    list_filter = ("rol",)