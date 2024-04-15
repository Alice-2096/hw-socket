import socket

# Set the server host and port
HOST, PORT = "localhost", 5000  # Replace with R3 ip addr 10.10.11.2

# Create a socket object and connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    # Specify the file name to send to the server
    client_file_name = "mytext.txt"
    # Read the file data
    with open(client_file_name, "rb") as file:
        file_data = file.read()
        # Send the file data to the server
        client_socket.sendall(file_data)

    print(f"File {client_file_name} sent to the server.")
