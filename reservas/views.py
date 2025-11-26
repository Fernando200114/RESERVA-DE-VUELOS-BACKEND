from django.http import JsonResponse

def home(request):
    return JsonResponse({"mensaje": "API de Reservas de Vuelos funcionando"})
