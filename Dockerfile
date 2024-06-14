# Usa una imagen base oficial de Python
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /code

# Copia el archivo de requisitos y los instala
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . /code/

# Expone el puerto 8000 para el servidor de desarrollo de Django
EXPOSE 8000

# Define el comando por defecto para ejecutar el servidor de desarrollo
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
