# Utilizar la imagen base oficial de PHP con Apache
FROM php:7.4-apache

# Copiar el archivo index.php al directorio de trabajo del servidor web
COPY index.php /var/www/html/

# Configurar el nombre del servidor en Apache
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Instalar cURL
RUN apt-get update && apt-get install -y libcurl4-openssl-dev pkg-config libssl-dev && docker-php-ext-install curl
