# Importamos FastAPI y utilidades

# APIRouter define rutas, Depends inyecta dependencias, HTTPException lanza errores HTTP
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from repositorios.tipo_cuenta_repository import TipoCuentaRepository
from servicios.tipo_cuenta_service import TipoCuentaService
from modelos.schemas.tipo_cuenta_schema import (
    TipoCuentaCreate,
    TipoCuentaListResponse,
    TipoCuentaSingleResponse,
    Respuesta,
)

# Creamos un router con prefijo y etiqueta
router = APIRouter(
    prefix="/api/tiposCuenta",
    tags=["Tipos Cuenta"],
    responses={
        200: {"description": "Operación exitosa"},
        404: {"description": "No encontrado"},
        422: {"description": "Solicitud incorrecta"},
        500: {"description": "Error del servidor"},
    },
)


# Dependencia para inyectar el servicio en cada endpoint
def get_service(db: Session = Depends(get_db)):
    try:
        repo = TipoCuentaRepository(db)  # Crea el repositorio con la sesión
        return TipoCuentaService(repo)  # Devuelve el servicio
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al inicializar el servicio: {str(e)}"
        )


# Endpoint GET para listar todos los tipos de cuenta
@router.get("/all", response_model=TipoCuentaListResponse)
def listar_tipos(Activos: bool, service: TipoCuentaService = Depends(get_service)):
    try:
        tipos = service.listar_tipos(Activos)
        return {
            "tipoCuenta": tipos,
            "respuesta": {"codigo": 200, "mensaje": "Consulta exitosa"},
        }
    except Exception as e:
        return {
            "tipoCuenta": None,
            "respuesta": {
                "codigo": 500,
                "mensaje": "Error al obtener tipo de cuenta: {str(e)}",
            },
        }


# Endpoint GET para obtener un tipo de cuenta por ID
@router.get("/id", response_model=TipoCuentaSingleResponse)
def obtener_tipo(id: int, service: TipoCuentaService = Depends(get_service)):
    try:
        tipo = service.obtener_tipo(id)  # Busca el tipo de cuenta por ID

        if not tipo:  # Si no existe, devuelve respuesta 404
            return {
                "tipoCuenta": None,
                "respuesta": {"codigo": 404, "mensaje": "Tipo de cuenta no encontrado"},
            }
        else:
            return {
                "tipoCuenta": tipo,
                "respuesta": {"codigo": 200, "mensaje": "Consulta exitosa"},
            }
    except Exception as e:
        return {
            "tipoCuenta": None,
            "respuesta": {
                "codigo": 500,
                "mensaje": "Error al obtener tipo de cuenta: {str(e)}",
            },
        }


# Endpoint POST para crear un nuevo tipo de cuenta
@router.post("/add", response_model=Respuesta)
def crear_tipo(
    tipo_data: TipoCuentaCreate, service: TipoCuentaService = Depends(get_service)
):
    try:
        # if exists := service.obtener_tipo(tipo_data.IdTipoCuenta):
        #     return {
        #         "respuesta": {
        #             "codigo": 400,
        #             "mensaje": "El IdTipoCuenta ya existe. No se pueden crear registros duplicados.",
        #         },
        #     }

        Respuesta = service.crear_tipo(tipo_data)
        if Respuesta:
            return {
                "respuesta": {
                    "codigo": 200,
                    "mensaje": "Tipo de cuenta creado exitosamente.",
                },
            }
        else:
            return {
                "respuesta": {
                    "codigo": 500,
                    "mensaje": "Tipo de cuenta no creado.",
                },
            }
    except Exception as e:
        return {
            "tipoCuenta": None,
            "respuesta": {
                "codigo": 500,
                "mensaje": "Error al obtener tipo de cuenta: {str(e)}",
            },
        }


# Endpoint PUT para actualizar un tipo de cuenta existente
@router.put("/update", response_model=Respuesta)
def actualizar_tipo(
    id: int,
    tipo_data: TipoCuentaCreate,
    service: TipoCuentaService = Depends(get_service),
):
    try:
        tipo = service.actualizar_tipo(id, tipo_data)

        if not tipo:  # Si no existe, lanza error 404
            return {
                "respuesta": {
                    "codigo": 500,
                    "mensaje": f"Tipo de cuenta no encontrado",
                },
            }
        else:
            return {
                "respuesta": {
                    "codigo": 201,
                    "mensaje": f"Tipo de cuenta actualizado exitosamente",
                },
            }
    except Exception as e:
        return {
            "respuesta": {
                "codigo": 500,
                "mensaje": f"Error al actualizar tipo de cuenta: {str(e)}",
            },
        }


# Endpoint DELETE para eliminar un tipo de cuenta
@router.delete("/delete", response_model=Respuesta)
def eliminar_tipo(id: int, service: TipoCuentaService = Depends(get_service)):
    try:
        tipo = service.eliminar_tipo(id)  # Elimina el registro
        if not tipo:  # Si no existe, lanza error 404
            return {
                "respuesta": {
                    "codigo": 500,
                    "mensaje": "Tipo de cuenta no encontrado",
                },
            }
        else:
            return {
                "respuesta": {
                    "codigo": 200,
                    "mensaje": "Tipo de cuenta eliminado exitosamente",
                },
            }  # Devuelve el registro eliminado
    except Exception as e:
        return {
            "respuesta": {
                "codigo": 500,
                "mensaje": f"Error al eliminar tipo de cuenta: {str(e)}",
            },
        }
