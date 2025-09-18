# May want to look into using udp instead
# Maybe look into apis for socket servers
import socket

# Temp code to allow for .env file for local testing
from dotenv import load_dotenv
import os

load_dotenv()

# Sub out to read config file. Using env for local testing
HOST = os.getenv("IP_HOST")
PORT = 12345


class Server:
    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)

        print(f"Server listening on {HOST}:{PORT}")

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
