from os import stat
import socket

target = input("Enter the IP address to scan: ")
port = input("Enter the port range to scan (ex 5-200): ")

lowport = int(port.split("-")[0])
highport = int(port.split("-")[1])

print("Scanning host ", target, "from port", lowport, "to port", highport)

for port in range(lowport, highport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if(status == 0):
        print("*** Port", port, "- OPEN ***")
    else:
        print("Port", port, "- CLOSED")

s.close()