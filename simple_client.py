import socket

SVR_ADDR = input("Type the server IP address: ")
SVR_PORT = int(input("Type the server port: "))

# create a socket object over TCP (SOCK_STREAM, SOCK_DGRAM for UDP)
my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client (comment out section for UDP as it is connectionless)
my_sock.connect((SVR_ADDR, SVR_PORT))
print("Connection established")

message = input("Message to send: ")
# send some data
my_sock.sendall(message.encode())

my_sock.close()
