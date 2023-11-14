import random
import string
from collections import OrderedDict
import socket
from threading import Thread

# Generate a random substitution cipher and save it to ensure it's static for each run
def generate_cipher():
    letters = string.ascii_lowercase
    shuffled_letters = list(letters)
    random.shuffle(shuffled_letters)
    cipher_map = OrderedDict(zip(letters, shuffled_letters))
    return cipher_map

# Encrypt the message using the generated cipher
def encrypt_message(message, cipher_map):
    encrypted_message = ""
    for char in message.lower():
        if char in cipher_map:
            encrypted_message += cipher_map[char]
        else:
            encrypted_message += char
    return encrypted_message

# Read the flag and append some text
def read_flag_with_context():
    with open('flag.txt', 'r') as file:
        flag = file.read().strip()
    return f"Frequency analysis can be very useful here. In english text some alphabets are used more than others. The secret message is: {flag}."

# Handle client connection
def handle_client(conn, addr, cipher_map):
    try:
        welcome_message = "Welcome to the Substitute Spy Encryption Service!\n"
        welcome_message += "Enter any text and see how it gets encrypted with our special cipher.\n"
        welcome_message += "Try to figure out the mapping to decrypt the flag.\n"
        welcome_message += "Type 'QUIT' to exit.\n\n"
        conn.sendall(welcome_message.encode())

        # Send the encrypted paragraph with the flag on connection
        paragraph_with_flag = read_flag_with_context()
        encrypted_paragraph = encrypt_message(paragraph_with_flag, cipher_map)
        conn.sendall(f"Encrypted Message: {encrypted_paragraph}\n".encode())

        # Interaction loop
        while True:
            conn.sendall(b"Enter text to encrypt: ")
            data = conn.recv(1024)
            if not data or data.strip().upper() == b'QUIT':
                break

            text_to_encrypt = data.decode().strip()
            encrypted_text = encrypt_message(text_to_encrypt, cipher_map)
            conn.sendall(f"Encrypted: {encrypted_text}\n".encode())
    except Exception as e:
        print(f"An error occurred with client {addr}: {e}")
    finally:
        conn.close()

# Set up server
def start_server(port, cipher_map):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        s.listen()

        print(f"Server listening on port {port}...")
        while True:
            conn, addr = s.accept()
            client_thread = Thread(target=handle_client, args=(conn, addr, cipher_map))
            client_thread.start()


# Main function to initiate the service
def main():
    port = 9999
    cipher_map = generate_cipher()
    start_server(port, cipher_map)

if __name__ == "__main__":
    main()
