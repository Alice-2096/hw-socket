import socketserver
import signal


def contains_secret(s):
    secret_index = 0
    secret = "SECRET"
    for char in s:
        if char == secret[secret_index]:
            secret_index += 1
            if secret_index == len(secret):
                return True

    return False


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip().decode("utf-8")
        # check if data contains "SECRET" as a subsequence
        if not contains_secret(self.data):
            self.request.sendall(b"Received: Secret code not found!")
        else:
            # return all digits in string and their count
            digits = "".join([char for char in self.data if char.isdigit()])
            num = len(digits)
            self.request.sendall(
                f"Received: Digits - {digits}, Total - {num}".encode("utf-8"))


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 5001

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        # Define a signal handler for Ctrl+C
        def signal_handler(sig, frame):
            print("\nShutting down server...")
            server.shutdown()  # Gracefully shut down the server
            server.server_close()  # Close the server socket
            print("Server shutdown complete.")
            exit(0)  # Exit the program

        # Set the signal handler for Ctrl+C
        signal.signal(signal.SIGINT, signal_handler)

        server.serve_forever()
