# Documentación del Proyecto: Gestor de Tareas

## Descripción General

Este proyecto es una aplicación web de gestión de tareas desarrollada en Django 5.2.7. Permite a los usuarios registrarse, autenticarse y gestionar sus tareas personales de manera segura y eficiente.

## Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas y aplicaciones:

```
M6_Evaluacion_modulo/
├── env/                    # Entorno virtual de Python
├── gestor/                 # Proyecto principal Django
│   ├── manage.py          # Comando principal de Django
│   ├── db.sqlite3         # Base de datos SQLite
│   ├── gestor/            # Configuración del proyecto
│   │   ├── settings.py    # Configuración principal
│   │   ├── urls.py        # URLs principales
│   │   ├── wsgi.py        # Configuración WSGI
│   │   └── asgi.py        # Configuración ASGI
│   ├── app_login/         # Aplicación de autenticación
│   │   ├── models.py      # Modelo de usuario personalizado
│   │   ├── views.py       # Vistas de login/registro/logout
│   │   ├── urls.py        # URLs de autenticación
│   │   ├── mixins.py      # Mixins para permisos
│   │   └── templates/     # Plantillas HTML
│   └── tareas/            # Aplicación de gestión de tareas
│       ├── models.py      # Modelo de tareas
│       ├── views.py       # Vistas CRUD de tareas
│       ├── forms.py       # Formularios de tareas
│       ├── urls.py        # URLs de tareas
│       └── templates/     # Plantillas HTML
```

## Funcionalidades Principales

### 1. Sistema de Autenticación
- **Registro de usuarios**: Creación de nuevas cuentas con validación
- **Login/Logout**: Inicio y cierre de sesión seguro
- **Usuario personalizado**: Modelo extendido con permisos específicos
- **Seguridad**: Sesiones con tiempo de expiración y protección CSRF

### 2. Gestión de Tareas (CRUD Completo)
- **Crear tareas**: Formulario para agregar nuevas tareas
- **Listar tareas**: Vista de todas las tareas del usuario
- **Editar tareas**: Modificación de tareas existentes
- **Eliminar tareas**: Eliminación segura con confirmación
- **Ver detalles**: Vista detallada de cada tarea

### 3. Características de las Tareas
- **Nombre**: Título descriptivo de la tarea
- **Descripción**: Detalle completo de la tarea
- **Fecha de creación**: Automática al crear la tarea
- **Fecha de vencimiento**: Fecha límite para completar
- **Estado**: Completada o pendiente
- **Usuario**: Asociación con el usuario propietario

### 4. Sistema de Permisos
- Permisos granulares por usuario:
  - `ver_tareas`: Visualizar tareas
  - `crear_tareas`: Crear nuevas tareas
  - `editar_tareas`: Modificar tareas existentes
  - `eliminar_tareas`: Eliminar tareas

### 5. Seguridad
- **Autenticación obligatoria**: Todas las rutas protegidas requieren login
- **Aislamiento de datos**: Cada usuario solo ve sus propias tareas
- **Validación de permisos**: Verificación de permisos en cada acción
- **Protección CSRF**: Seguridad contra ataques de falsificación

## Instalación y Configuración

### Prerrequisitos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (opcional, para clonar el repositorio)

### 1. Clonar el Repositorio
```bash
git clone https://github.com/Matiaslagost7/M6_Evaluacion_modulo.git
cd M6_Evaluacion_modulo
```

### 2. Crear y Activar el Entorno Virtual

#### En Windows (PowerShell):
```powershell
# Crear entorno virtual
python -m venv env

# Activar entorno virtual
.\env\Scripts\Activate.ps1

# Si hay problemas de permisos, ejecutar:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### En Linux/macOS:
```bash
# Crear entorno virtual
python3 -m venv env

# Activar entorno virtual
source env/bin/activate
```

### 3. Instalar Dependencias
```bash
pip install django==5.2.7
pip install pillow
```

### 4. Configurar la Base de Datos

#### Navegar al directorio del proyecto:
```bash
cd gestor
```

#### Ejecutar migraciones:
```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones a la base de datos
python manage.py migrate

# Crear superusuario (opcional)
python manage.py createsuperuser
```

### 5. Ejecutar el Servidor de Desarrollo
```bash
python manage.py runserver
```

El proyecto estará disponible en: `http://127.0.0.1:8000/`

## Uso de la Aplicación

### 1. Acceso Inicial
- Visita `http://127.0.0.1:8000/`
- Si no estás autenticado, serás redirigido a `/login/`

### 2. Registro de Usuario
- Accede a `/register/`
- Completa el formulario con:
  - Nombre de usuario
  - Email
  - Nombre y apellido
  - Contraseña (dos veces para confirmación)

### 3. Gestión de Tareas
Una vez autenticado, puedes:
- **Ver todas tus tareas**: Página principal `/`
- **Crear nueva tarea**: `/tasks/create/`
- **Editar tarea**: `/tasks/<id>/update/`
- **Ver detalles**: `/tasks/<id>/`
- **Eliminar tarea**: `/tasks/<id>/delete/`

### 4. Panel de Administración
- Accede a `/admin/` con credenciales de superusuario
- Gestiona usuarios y tareas desde la interfaz administrativa

## Usuarios de Prueba

El sistema incluye usuarios preconfigurados para facilitar las pruebas y demostración:

### Usuarios Regulares
Usuarios que pueden ingresar, crear, editar y eliminar tareas:

- **Usuario**: `Mati2`
  - **Contraseña**: `Trabajo2000`
  
- **Usuario**: `Mati1`
  - **Contraseña**: `Mati2000`

### SuperUsuario
Usuario administrador con acceso completo al panel de administración:

- **SuperUser**: `Mati10`
  - **Contraseña**: `Mati2000`

> **Nota**: Estos usuarios están disponibles para pruebas. En producción, asegúrate de cambiar las contraseñas por defecto y crear usuarios personalizados según tus necesidades.

## URLs Principales

| URL | Descripción | Requiere Autenticación |
|-----|-------------|----------------------|
| `/` | Página principal con lista de tareas | Sí |
| `/login/` | Inicio de sesión | No |
| `/register/` | Registro de usuario | No |
| `/logout/` | Cerrar sesión | Sí |
| `/tasks/` | Lista completa de tareas | Sí |
| `/tasks/create/` | Crear nueva tarea | Sí |
| `/tasks/<id>/` | Ver detalles de tarea | Sí |
| `/tasks/<id>/update/` | Editar tarea | Sí |
| `/tasks/<id>/delete/` | Eliminar tarea | Sí |
| `/admin/` | Panel de administración | Sí (superusuario) |

## Configuración Adicional

### Variables de Entorno (Producción)
Para producción, considera configurar:
- `SECRET_KEY`: Clave secreta única
- `DEBUG = False`: Desactivar modo debug
- `ALLOWED_HOSTS`: Lista de hosts permitidos
- Base de datos PostgreSQL o MySQL

### Configuración de Seguridad
El proyecto incluye configuraciones de seguridad:
- Sesiones expiran en 1 hora
- Sesiones se cierran al cerrar el navegador
- Hashers de contraseñas seguros (PBKDF2)

## Solución de Problemas Comunes

### 1. Error al activar entorno virtual en Windows
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. Error "No module named 'django'"
```bash
# Asegúrate de que el entorno virtual esté activado
pip install django==5.2.7
```

### 3. Error de migraciones
```bash
# Eliminar migraciones y recrear
rm -rf app_login/migrations/
rm -rf tareas/migrations/
python manage.py makemigrations app_login
python manage.py makemigrations tareas
python manage.py migrate
```

### 4. Problemas de permisos
- Verifica que el usuario tenga los permisos necesarios
- Usa el panel de administración para asignar permisos

## Tecnologías Utilizadas

- **Backend**: Django 5.2.7
- **Frontend**: HTML5, CSS3, Bootstrap (parcial)
- **Base de Datos**: SQLite (desarrollo), compatible con PostgreSQL/MySQL
- **Autenticación**: Sistema integrado de Django con usuario personalizado
- **Seguridad**: CSRF protection, sesiones seguras, permisos granulares

## Contribuciones

Para contribuir al proyecto:
1. Haz fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Crea un Pull Request

## Licencia

Este proyecto es de uso educativo y está disponible bajo licencia MIT.

---

**Autor**: Matías Lagos  
**Fecha**: Octubre 2025  
**Versión**: 1.0