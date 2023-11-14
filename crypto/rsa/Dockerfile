# Use an appropriate base image, e.g. python:3.9
FROM python:3.9-slim

# Set working directory in container
WORKDIR /app


# Combine apt-get operations and cleanup in the same RUN command
# Also install python packages in the same step
RUN apt-get update -y && \
    apt-get install -y socat && \
    pip install pycryptodome && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Copy the Python script to the container
COPY challenge.py .
COPY flag.txt .


# Expose the desired port
EXPOSE 9999/TCP


CMD ["socat", "TCP-LISTEN:9999,fork,reuseaddr", "EXEC:python3 /app/challenge.py"]