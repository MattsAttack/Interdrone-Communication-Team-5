# Server is just writing data to a file

# May want to look into using udp instead
import socket


class Server:
    def __init__(self, jsonData):
        self.jsonData = jsonData

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Update to take specific drone value (EX: Drone 2)
        server_socket.bind(
            (
                str(self.jsonData["drones"]["drone1"]["ip"]),
                int(self.jsonData["drones"]["drone1"]["port"]),
            )
        )
        server_socket.listen(5)

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
