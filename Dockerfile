# Primera etapa: Construir la aplicación
FROM python:slim as build

WORKDIR /app
ADD . /app
COPY . .
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt

# Segunda etapa: Imagen final de ejecución
FROM build as runtime
EXPOSE 5000
EXPOSE 27017

# Comando para iniciar la aplicación
CMD ["python", "app.py"]
