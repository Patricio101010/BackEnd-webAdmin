# Importaciones necesarias para la configuración de SQLAlchemy asincrónico
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config.settings import settings

# Configuración del motor de base de datos asincrónico
# - Utiliza la URL de conexión desde las variables de configuración
# - echo=True: registra todas las sentencias SQL ejecutadas (útil para debugging)
# - pool_pre_ping=True: verifica la conexión antes de usarla para evitar errores de conexión cerrada
engine = create_async_engine(
    settings.database_url,
    echo=True,
    pool_pre_ping=True,
)

# Crear una fábrica de sesiones asíncronas para gestionar conexiones a la base de datos
# - expire_on_commit=False: mantiene los objetos sin expirar después de hacer commit
AsyncSessionLocal = async_sessionmaker(
    engine,
    expire_on_commit=False,
)

# Función generadora que proporciona una sesión de base de datos asincrónica
# Se utiliza como dependencia en los endpoints FastAPI para inyectar la sesión
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
