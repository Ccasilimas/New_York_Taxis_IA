FROM public.ecr.aws/lambda/python:3.8

# Crear un directorio de trabajo
WORKDIR /var/task

# Copiar el archivo requirements.txt
COPY requirements.txt .

# Instalar dependencias
RUN pip install -r requirements.txt -t python/

# Empaquetar dependencias en un archivo zip
RUN zip -r /layer.zip python
