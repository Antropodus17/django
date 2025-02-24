# Usa una imagen base oficial de Python
FROM python:3.11


# RUN apt update && apt install -y nodejs npm



# Establece el directorio de trabajo dentro del contenedor
WORKDIR /code

# Copia el archivo de requisitos al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código del proyecto al directorio de trabajo en el contenedor
COPY ./code/ /code/


# Añade alias basicos para el django
RUN echo 'alias makemigrations="python3 manage.py makemigrations"' >> /root/.bashrc
RUN echo 'alias migrate="python3 manage.py migrate"' >> /root/.bashrc
RUN echo 'alias shell="python3 manage.py shell"' >> /root/.bashrc
RUN echo 'alias runserver="python3 manage.py runserver"' >> /root/.bashrc
RUN echo 'alias createsuperuser="python3 manage.py createsuperuser"' >>/root/.bashrc
RUN echo 'alias help="python3 manage.py help"' >> /root/.bashrc
RUN echo 'alias pm="python3 manage.py"' >> /root/.bashrc

# Ejecuta el comando para crear un nuevo proyecto Django
# RUN django-admin startproject password_generator .

# Expone el puerto que Django usa por defecto
# EXPOSE 8000

# Comando por defecto para ejecutar cuando se inicie el contenedor
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
