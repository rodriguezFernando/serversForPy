import socket
import select

sockets = []

for port in range(8000,8003):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('192.168.1.172', port))
    sockets.append(server_socket)

empty = []
while True:
    readable, writable, exceptional = select.select(sockets, empty, empty)
    for s in readable:
         (client_data, client_address) = s.recvfrom(65536)
         print(client_address, client_data)
    for s in sockets:
        s.close()