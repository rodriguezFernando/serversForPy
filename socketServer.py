import socket

#
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("192.168.100.19", 8080))

while True:
       data, addr = server_socket.recvfrom(65536) 
       text = data.decode('ascii')
       print("received message {} from {}".format(text, addr))
       
       