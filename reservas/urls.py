from django.contrib import admin
from django.urls import path, include
from . import views  # si tienes home
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("", views.home),  # home o incios 
    path("admin/", admin.site.urls),
    path("api/", include("vuelos.urls")),  # tus endpoints
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  # login JWT
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),   # refresh token
]
