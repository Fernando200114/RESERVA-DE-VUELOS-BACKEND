from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Llama al manejador por defecto
    response = exception_handler(exc, context)

    if response is not None:
        # Formato consistente para todos los errores
        response.data['status_code'] = response.status_code
        response.data['detalle'] = response.data.get('detail', '')
    
    return response
