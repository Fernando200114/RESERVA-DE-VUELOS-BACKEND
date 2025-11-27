# Sistema de Reservas de Vuelos

## Descripción
Sistema REST en Django para gestionar vuelos

## Tecnologías
- Python 
- Django 
- Django REST Framework
- PostgreSQL
- djangorestframework-simplejwt
- django-filters

## Instalación

# Entorno virtual 
python -m venv venv
venv\Scripts\activate

#Instalar dependencias 
pip install -r requirements.txt

# Crear variables de entorno 
DB_NAME=nombre_db
DB_USER=usuario
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432

# Migrar base de datos 
python manage.py migrate

# Creación de super usuario 
# Con este usuario colocamos en postman para crear el token con el usuario y contraseña 
# Correspondiente poara validar el token 
python manage.py createsuperuser

POST /api/token/
Body:
{
  "username": "info",
  "password": "info"
}

Endpoints

Aerolíneas

Listar: GET 
Crear: POST 
Detalle: GET 
Actualizar: PUT 
Eliminar: DELETE

Aviones

Listar: GET 
Crear: POST 
Detalle: GET 
Actualizar: PUT 
Eliminar: DELETE 

Vuelos

Listar: GET
Crear: POST 
Detalle: GET 
Actualizar: PUT
Eliminar: DELETE 

Pasajeros

Listar: GET 
Crear: POST 
Detalle: GET 
Actualizar: PUT
Eliminar: DELETE

Reservas
Listar: GET 
Crear: POST 
Detalle: GET 
Actualizar: PUT
Eliminar: DELETE 

Tripulación
Listar: GET 
Crear: POST
Detalle: GET 
Atualizar: PUT 
Eliminar: DELETE
