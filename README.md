# Biblioteca Django

Este proyecto es una aplicación de biblioteca construida con Django, que permite gestionar libros, autores y reservas. También incluye un API REST para interactuar con los datos de libros, autores y reservas.

## Requisitos

- Python 3.11
- Django 4.x
- Django REST framework
- Django REST framework Authtoken

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tuusuario/biblioteca.git
    cd biblioteca
    ```

2. Crea y activa un entorno virtual:

    En Windows:
    ```bash
    python -m venv djenv
    .\djenv\Scripts\activate
    ```

    En macOS/Linux:
    ```bash
    python3 -m venv djenv
    source djenv/bin/activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Crea un superusuario para acceder al panel de administración de Django:

    ```bash
    python manage.py createsuperuser
    ```

6. Ejecuta el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

7. Accede a la aplicación en tu navegador en `http://127.0.0.1:8000/`.

## Uso

### API REST

La aplicación incluye un API REST para gestionar libros, autores y reservas. Los endpoints principales son:

- **Autores**: `/api/autores/`
- **Libros**: `/api/libros/`
- **Reservas**: `/api/reservas/`

#### Obtener Token de Autenticación

Para interactuar con el API, primero debes obtener un token de autenticación. Envía una solicitud POST con tu nombre de usuario y contraseña a:

```bash
curl -X POST -d "username=tuusuario&password=tupassword" http://127.0.0.1:8000/api-token-auth/
