# Finanza-web-app

API para la gestión de finanzas personales e inversiones, construida con FastAPI y diseñada para ser rápida, escalable y fácil de mantener.
---

## 🚀 Tecnologías

**Backend:**
- 🐍 **Python 3.10+**
- ⚡ **Framework:** FastAPI
- 🗃️ **ORM:** SQLAlchemy 2.0
- 🗄️ **DB inicial:** SQL Server
- 🔁 **Migraciones:** Alembic
- 🔐 **Auth:** JWT (OAuth2PasswordBearer)
- 🧬 **Config:** Pydantic Settings
- 🧪 **Tests:** Pytest + httpx
- 🐳 **Docker:** Entorno reproducible y despliegue
---

## 🧱 Estructura del Proyecto

### Backend 
```
mi_app/
│
├── main.py                     # Punto de entrada
├── config/                     # Configuración
│   ├── __init__.py
│   ├── settings.py            # Variables de entorno y configuración
│   └── database.py            # Configuración específica de DB
├── api/                       # Capa de presentación
│   ├── __init__.py
│   ├── routes/                # Rutas organizadas por módulo
│   │   ├── __init__.py
│   │   ├── usuarios.py
│   │   └── auth.py
│   └── dependencies.py        # Dependencias inyectables
├── core/                      # Núcleo de la aplicación
│   ├── __init__.py
│   ├── security.py            # Autenticación, JWT, hashing
│   └── exceptions.py          # Excepciones personalizadas
├── services/                  # Lógica de negocio
│   ├── __init__.py
│   ├── usuario_service.py
│   └── base_service.py        # Servicio base con operaciones CRUD
├── repositories/              # Patrón Repository
│   ├── __init__.py
│   ├── usuario_repository.py
│   ├── base_repository.py     # Repository base
│   └── interfaces/            # Interfaces/abstract classes
│       ├── __init__.py
│       └── usuario_repository_interface.py
├── models/                    # Modelos de datos
│   ├── __init__.py
│   ├── domain/                # Modelos de dominio
│   │   ├── __init__.py
│   │   └── usuario.py
│   ├── schemas/               # Esquemas Pydantic
│   │   ├── __init__.py
│   │   ├── usuario_schema.py
│   │   └── request_response.py # Schemas para request/response
│   └── enums/                 # Enumeraciones
│       ├── __init__.py
│       └── usuario_enum.py
├── db/                        # Configuración de base de datos
│   ├── __init__.py
│   ├── database.py            # Conexión y session factory
│   └── migrations/            # Migraciones (si usas Alembic)
├── utils/                     # Utilidades
│   ├── __init__.py
│   └── validators.py          # Validadores personalizados
├── tests/                     # Pruebas
│   ├── __init__.py
│   ├── conftest.py            # Configuración de pytest
│   ├── test_usuarios.py
│   └── integration/           # Pruebas de integración
└── requirements.txt

tests/                       # Pruebas unitarias e integración
requirements.txt             # Dependencias del proyecto
main.py                      # Punto de entrada de la API
Dockerfile                   # Imagen Docker para despliegue
```

🛠️ Instalación
Requisitos previos
Python 3.10+

(Opcional) Docker y Docker Compose

Instalación local
```plaintext
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate     # En Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el servidor
uvicorn app.main:app --reload

```
📚 Documentación de la API
FastAPI genera documentación automática con Swagger UI y Redoc. Una vez que el servidor está corriendo, puedes acceder a:

http://localhost:8000/docs → Swagger UI

http://localhost:8000/redoc → Redoc

---

# 📦 Dependencias Principales
## Crear el proyecto base con FastAPI y SQLAlchemy:
```mkdir finanza-web-app
cd finanza-web-app
python -m venv venv
venv\Scripts\activate
```
## Comando pip install para instalar las dependencias principales:

``` plaintext
pip install fastapi uvicorn sqlalchemy pyodbc alembic pydantic-settings python-jose passlib[bcrypt] pytest httpx
```

---
## Estructura de carpetas y archivos