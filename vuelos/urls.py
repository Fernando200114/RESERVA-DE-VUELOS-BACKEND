from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import AerolineaViewSet, AvionViewSet, VueloViewSet
from .views import VueloViewSet, PasajeroViewSet

router = DefaultRouter()
router.register(r"aerolineas", AerolineaViewSet, basename="aerolineas")
router.register(r"aviones", AvionViewSet, basename="aviones")
router.register(r"vuelos", VueloViewSet, basename="vuelos")
router.register(r'pasajeros', PasajeroViewSet)

urlpatterns = [
    path("", include(router.urls)),
]


from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    AerolineaViewSet,
    AvionViewSet,
    VueloViewSet,
    PasajeroViewSet,
    ReservaViewSet,
    TripulacionViewSet,
)

router = DefaultRouter()
router.register(r"aerolineas", AerolineaViewSet, basename="aerolineas")
router.register(r"aviones", AvionViewSet, basename="aviones")
router.register(r"vuelos", VueloViewSet, basename="vuelos")
router.register(r"pasajeros", PasajeroViewSet, basename="pasajeros")
router.register(r"reservas", ReservaViewSet, basename="reservas")
router.register(r"tripulacion", TripulacionViewSet, basename="tripulacion")


urlpatterns = [
    path("", include(router.urls)),
]

