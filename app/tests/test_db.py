# RUTA: app/tests/test_db.py
import asyncio
from db.database import engine

async def test():
    async with engine.connect() as conn:
        print("Conectado OK")

asyncio.run(test())
