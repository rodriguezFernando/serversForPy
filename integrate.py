import time
import serial
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('192.168.100.63', 8080))

serial_port = serial.Serial(
	port="/dev/ttyTHS1",
	baudrate=2000000,
	bytesize=serial.EIGHTBITS,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
)

time.sleep(1)
print('opening port 8080 on 192.168.100.63')
try:
	while True:
		data, address = server_socket.recvfrom(65536)
		text = data.decode("ascii")
		print(text)
		serial_port.write((f'{text}').encode())
		
except KeyboardInterrupt:
	print("Exiting Program")

except Exception as exception_error:
	print("Error occurred. Exiting Program")
	print("Error: " + str(exception_error))

finally:
	serial_port.close()
	pass
