# Use the official PHP image with Apache
FROM php:7.4-apache-bullseye

# Copy the source code to the www directory
COPY src/ /var/www/html/
COPY flag.txt /var/www/html/

# Set the permission of flag.txt
RUN chmod 444 /var/www/html/flag.txt && \
    chown www-data:www-data /var/www/html/*

# Expose port 80
EXPOSE 80

# Use the default Apache entrypoint
CMD ["apache2-foreground"]
