import socket


IP = socket.gethostbyname(socket.gethostname())
PORT = 5555 # following by Server port
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

# Socket for client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((IP, PORT))
