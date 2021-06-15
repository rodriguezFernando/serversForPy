import socket

UDP_serverIP = '192.168.1.172'
UDP_serverPORT = 8000 #modificar(escoger de 8000-8003)
MESSAGE = b"Hello, World from client # !"
   
print("UDP target IP: %s" % UDP_serverIP)
print("UDP target port: %s" % UDP_serverPORT)
print("message: %s" % MESSAGE)
  
socketServer = socket.socket(socket.AF_INET, 
                       socket.SOCK_DGRAM) 

socketServer.sendto(MESSAGE, (UDP_serverIP, UDP_serverPORT))