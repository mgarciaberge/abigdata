# Utilizamos la imagen de Python alpine como base
FROM python:3.11.8-alpine
# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app
# Copiamos el archivo de requisitos e instalamos las dependencias
COPY requeriments.txt /app
RUN pip install -r requeriments.txt
# Copiamos el resto del código de la aplicación
COPY . /app
ENV FLASK_APP=app.py
# Ejecutamos la aplicación Flask con el host establecido en 0.0.0.0
CMD flask run -h 0.0.0.0 -p 5000
# Exponemos el puerto 5000
EXPOSE 5000
