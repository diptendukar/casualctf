# Use the official Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python script and flag into the container
COPY substitution_cipher_service.py flag.txt /app/

# Expose the port the service will be running on
EXPOSE 9999

# Run the service
CMD ["python", "/app/substitution_cipher_service.py"]
