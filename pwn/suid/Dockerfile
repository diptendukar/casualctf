FROM ubuntu:20.04

# Install required packages
RUN apt-get update && apt-get install -y socat


# Create a non-root user
RUN useradd -m ctf

# Set work directory
WORKDIR /home/ctf

# Copy the source code and the flag
COPY suid_reader /home/ctf
COPY flag.txt /home/ctf

RUN chown root:root /home/ctf/suid_reader
RUN chmod 755 /home/ctf/suid_reader
RUN chmod u+s /home/ctf/suid_reader

RUN mkdir /opt/reader/
RUN mv /home/ctf/suid_reader /opt/reader/suid_reader
RUN chown root:root /home/ctf/flag.txt 
RUN chmod 700 /home/ctf/flag.txt 


# Change to the ctf user
USER ctf

EXPOSE 9999

ENTRYPOINT ["socat", "TCP-LISTEN:9999,reuseaddr,fork", "EXEC:'/bin/bash -i',pty,stderr,setsid,sigint,sane"]

