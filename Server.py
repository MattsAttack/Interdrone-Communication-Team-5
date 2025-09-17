import socket

# Temp code to allow for .env file for local testing
from dotenv import load_dotenv
import os

load_dotenv()

# Sub out to read config file. Using env for local testing
host = os.getenv("IP_ADDRESS")
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

try:
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection accepted from {client_address}")

        data = client_socket.recv(1024)
        print(f"Received from client: {data.decode()}")

        response = "Server received your message!"
        client_socket.sendall(response.encode())

        client_socket.close()
except KeyboardInterrupt:
    print("Server shutting down.")
finally:
    server_socket.close()
