FROM ubuntu:20.04

# Install required packages
RUN apt-get update && apt-get install -y \
    bash \
    coreutils \
    socat

# Create a non-root user
RUN useradd -m ctf

# Set work directory
WORKDIR /home/ctf

# Copy the restricted shell script
COPY restricted_shell.sh /home/ctf
COPY flag.txt /home/ctf

# Set the appropriate permissions
RUN chmod +x /home/ctf/restricted_shell.sh

# Change the owner of the flag to root and make it readable only by root and ctf user
RUN chown root:ctf /home/ctf/flag.txt && chmod 440 /home/ctf/flag.txt

# Change the owner of the script to root and make it executable but not readable or writable by others
RUN chown root:root /home/ctf/restricted_shell.sh && chmod 755 /home/ctf/restricted_shell.sh

RUN mv /home/ctf/restricted_shell.sh /etc/restricted_shell.sh


# Switch to the non-root user
USER ctf

# Set up the environment
ENV TERM=xterm-256color

EXPOSE 9999

# Use socat to listen on port 9999 and execute the restricted shell when a connection is made
ENTRYPOINT ["socat", "TCP-LISTEN:9999,reuseaddr,fork", "EXEC:'/etc/restricted_shell.sh -i',pty,stderr,setsid,sigint,sane"]
