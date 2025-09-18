import socket
import time

# Temp code to allow for .env file for local testing
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("IP_HOST")  # The server's hostname or IP address
PORT = 12345  # The port used by the server


class Client:
    def start_client(self):
        while True:
            print("starting thread")
            self.send_data(serverIP="10.110.5.136", serverPort=12345)
            time.sleep(5)

    def send_data(self, serverIP: str, serverPort: int):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((serverIP, serverPort))
            client_socket.sendall(b"Hello, server!")
            data = client_socket.recv(1024)
            print(f"Received from server: {data.decode()}")
