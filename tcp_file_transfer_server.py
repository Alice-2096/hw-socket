import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):

    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # Receive file data from the client
        file_data = self.request.recv(1024)
        # Specify the file name on the server side
        server_file_name = "received_file.txt"
        with open(server_file_name, "wb") as file:
            while file_data:
                file.write(file_data)
                file_data = self.request.recv(1024)


if __name__ == "__main__":
    # Set the server host and port
    HOST, PORT = "0.0.0.0", 5000

    # Create the TCP server
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
