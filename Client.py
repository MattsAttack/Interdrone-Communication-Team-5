import socket

# Temp code to allow for .env file for local testing
from dotenv import load_dotenv
import os

load_dotenv()


HOST = os.getenv("IP_HOST")  # The server's hostname or IP address
PORT = 12345  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.sendall(b"Hello, server!")
    data = client_socket.recv(1024)
    print(f"Received from server: {data.decode()}")
