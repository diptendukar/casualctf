# Use the official PHP image with Apache
FROM php:7.4-apache

# Install ping utility
RUN apt-get update && \
    apt-get install -y --no-install-recommends iputils-ping && \
    rm -rf /var/lib/apt/lists/*

# Copy the source code to the www directory
COPY index.php /var/www/html/
COPY flag.txt /var/www/

# Set the permission of flag.txt
RUN chmod 444 /var/www/flag.txt && \
    chown www-data:www-data /var/www/html/*

# Expose port 80
EXPOSE 80

# Use the default Apache entrypoint
CMD ["apache2-foreground"]