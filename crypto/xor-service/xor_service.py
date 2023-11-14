import os
import socket
from threading import Thread
import time

# Generate a random 8-byte key
key = os.urandom(8)

# XOR the given message with the key
def xor_encrypt_decrypt(message, key):
    return bytes([message[i] ^ key[i % len(key)] for i in range(len(message))])

# Read the flag and encrypt it
def read_and_encrypt_flag():
    with open('flag.txt', 'r') as file:
        flag = file.read().strip().encode()
    return xor_encrypt_decrypt(flag, key)

# Handle client connection
def handle_client(conn, addr):
    try:
        welcome_message = "Welcome to the XOR Cipher Service!\n"
        welcome_message += "You can encrypt a message using our service.\n"
        welcome_message += "Enter text and receive the encrypted version.\n"
        welcome_message += "Find the key to decrypt the flag.\n"
        welcome_message += "The key is 8 random bytes.\n"
        welcome_message += "Type 'QUIT' to exit.\nGood Luck!\n\n"
        conn.sendall(welcome_message.encode())

        conn.sendall(f"Generating random key\n".encode())
        time.sleep(1)
        conn.sendall(f"Encrypting flag with key\n".encode())
        time.sleep(1)
        # Send the encrypted flag on connection
        encrypted_flag = read_and_encrypt_flag()
        conn.sendall(f"Encrypted Flag: {encrypted_flag.hex()}\n".encode())

        # Interaction loop
        while True:
            conn.sendall(b"Enter text to encrypt: ")
            data = conn.recv(1024)
            if not data or data.strip().upper() == b'QUIT':
                break

            text_to_encrypt = data.decode().strip()
            encrypted_result = xor_encrypt_decrypt(text_to_encrypt.encode(), key)
            conn.sendall(f"Encrypted Result: {encrypted_result.hex()}\n".encode())
    except Exception as e:
        print(f"An error occurred with client {addr}: {e}")
    finally:
        conn.close()

# Set up server
def start_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen()

        print(f"Server listening on port {port}...")
        while True:
            conn, addr = s.accept()
            client_thread = Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

# Main function to initiate the service
def main():
    port = 9999
    start_server(port)

if __name__ == "__main__":
    main()
