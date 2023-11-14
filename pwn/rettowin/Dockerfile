# First stage: Build environment with Ubuntu
FROM ubuntu:20.04 as ret2win

# Install build dependencies
RUN apt-get update && apt-get install -y \
    socat \
    gcc-multilib \
    make

# Copy source files
WORKDIR /build
COPY challenge.c .
COPY Makefile .

# Build the challenge
RUN make

# Second stage: 
FROM ubuntu:20.04

# Install runtime dependencies
RUN apt-get update && apt-get install -y socat

# Create non-root user
RUN useradd -m pwn

WORKDIR /home/pwn

# Copy the compiled binary from the builder stage
COPY --from=ret2win /build/challenge .

# Copy flag
COPY flag.txt .

# Set permissions
RUN chmod 111 challenge && \
    chmod 444 flag.txt

# Expose port and set the entry point
USER pwn
EXPOSE 9999
CMD ["socat", "TCP-LISTEN:9999,reuseaddr,fork", "EXEC:./challenge"]
