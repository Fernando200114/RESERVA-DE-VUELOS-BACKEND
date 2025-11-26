from django.db import models
from django.contrib.auth.models import User



class Aerolinea(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    pais = models.CharField(max_length=100)
    codigo_iata = models.CharField(max_length=3, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Aerolínea"
        verbose_name_plural = "Aerolíneas"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} ({self.codigo_iata})"


class Avion(models.Model):
    modelo = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    matricula = models.CharField(max_length=20, unique=True)
    fabricante = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Avión"
        verbose_name_plural = "Aviones"
        ordering = ["matricula"]

    def __str__(self):
        return f"{self.matricula} - {self.modelo}"


class Vuelo(models.Model):
    ESTADO_CHOICES = [
        ("Programado", "Programado"),
        ("Activo", "Activo"),
        ("Completado", "Completado"),
        ("Cancelado", "Cancelado"),
    ]

    numero_vuelo = models.CharField(max_length=20, unique=True)
    aerolinea = models.ForeignKey(Aerolinea, on_delete=models.PROTECT, related_name="vuelos")
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha_salida = models.DateField()
    hora_salida = models.TimeField()
    fecha_llegada = models.DateField()
    hora_llegada = models.TimeField()
    avion = models.ForeignKey(Avion, on_delete=models.SET_NULL, null=True, blank=True, related_name="vuelos")
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default="Programado")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Vuelo"
        verbose_name_plural = "Vuelos"
        ordering = ["fecha_salida", "hora_salida", "numero_vuelo"]

    def __str__(self):
        return f"{self.numero_vuelo} — {self.origen} → {self.destino}"


class Pasajero(models.Model):
    cedula = models.CharField(max_length=10, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "Pasajero"
        verbose_name_plural = "Pasajeros"
        ordering = ["apellidos", "nombres"]

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.cedula}"


class Reserva(models.Model):
    ESTADO_CHOICES = [
        ("Pendiente", "Pendiente"),
        ("Confirmada", "Confirmada"),
        ("Cancelada", "Cancelada"),
    ]

    codigo_reserva = models.CharField(max_length=10, unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reservas")
    vuelo = models.ForeignKey(Vuelo, on_delete=models.CASCADE, related_name="reservas")
    pasajero = models.ForeignKey(Pasajero, on_delete=models.CASCADE, related_name="reservas")
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    asiento = models.CharField(max_length=5, blank=True, null=True)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default="Pendiente")

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["-fecha_reserva"]

    def __str__(self):
        return f"{self.codigo_reserva} - {self.usuario.username}"


class Tripulacion(models.Model):
    ROLES_CHOICES = [
        ("Piloto", "Piloto"),
        ("Copiloto", "Copiloto"),
        ("Auxiliar", "Auxiliar"),
    ]

    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, choices=ROLES_CHOICES)
    avion = models.ForeignKey(Avion, on_delete=models.SET_NULL, null=True, blank=True, related_name="tripulacion")

    class Meta:
        verbose_name = "Tripulación"
        verbose_name_plural = "Tripulaciones"
        ordering = ["apellidos", "nombres"]

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.rol}"
