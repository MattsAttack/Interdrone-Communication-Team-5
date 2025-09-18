import threading
import server
import client
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(threadName)s - %(levelname)s - %(message)s",
)

# Instantiate Server and Client
serverInstance = server.Server()
clientInstance = client.Client()

# Create threads properly (don't call the functions with parentheses)
serverThread = threading.Thread(target=serverInstance.start_server, name="ServerThread")
clientThread = threading.Thread(target=clientInstance.start_client, name="ClientThread")

# Start the threads
serverThread.start()
print("Server started")
clientThread.start()
print("Client started")

# Wait for threads to complete (if needed)
serverThread.join()
clientThread.join()
