import socket
import threading

PORT = 5555 # You can change it as you like, don't forget PORT from c_socket.py must following from this server.py PORT

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Connected: {client_address}")

    # Receive and echo messages from client
    while True:
        pesan = client_socket.recv(1024).decode()
        if not pesan:
            break
        # print(f"Received from {client_address}: {message}")
        # Broadcast the message to all clients
        #broadcast(message)
        # broadcast(f"Received from {client_address}: {message}")

    # print(f"Disconnected: {client_address}")
    client_socket.close()
    
# Function to broadcast messages to all clients
def broadcast(pesan):   
    for client in clients:
        try:
            client.send(pesan.encode())
        except:
            # Remove the client if it's not reachable
            clients.remove(client)

# Create a socket for the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to a specific address and port
server.bind(('0.0.0.0', PORT))

# Listen for incoming connections
server.listen(5)
# print("Server listening for connections...")

# List to store client sockets
clients = []

# Accept and handle incoming connections
while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()