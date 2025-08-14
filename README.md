# Finanza-web-app

API para la gestión de finanzas personales e inversiones, construida con FastAPI y diseñada para ser rápida, escalable y fácil de mantener.
---

## 🚀 Tecnologías

**Backend:**
- 🐍 Python 3.10+
- ⚡ FastAPI (Framework web moderno y rápido)
- 🧬 Pydantic (Validación y serialización de datos)
- 🐳 Docker (Entorno reproducible y despliegue)
- 🧪 Pytest (Pruebas unitarias y de integración)
- 🗃️ ORM (SQLAlchemy o Tortoise, según tu elección)
---

## 🧱 Estructura del Proyecto

### Backend 
```plaintext
app/
├── models/                  # Modelos de datos (ORM o clases)
├── routes/                  # Endpoints y rutas HTTP
├── services/                # Lógica de negocio
└── schemas/                 # Validaciones (Pydantic o similar)

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

