FROM python:3.11-slim
WORKDIR /app

# Copiar y instalar dependencias
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

EXPOSE 8000

# Cambiar el path a app.main porque main.py está dentro de app/
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
