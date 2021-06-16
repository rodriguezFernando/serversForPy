import socket
import re

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('192.168.1.126', 8080))



while True:
 patterns=['<1.8.4.1>', 'Boton de paro']
 data, addr = server_socket.recvfrom(65536)
 text = data.decode('ascii')
 print("received message {} from {}".format(text, addr))
 for pattern in patterns:
	 if re.search(pattern, text):
	  print("match found")
	 else:
	  print("not found")   
