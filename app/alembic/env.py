from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context

from config.settings import settings
from db.base import Base

# IMPORTAR MODELOS
from models.domain.usuario import Usuario
