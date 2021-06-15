import time
import serial

print("UART Demonstration Program")


serial_port = serial.Serial(
	port="/dev/ttyTHS1",
	baudrate=2000000,
	bytesize=serial.EIGHTBITS,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
)
# Wait a second to let the port initialize
time.sleep(1)

try:
	# Send a simple header
	print("Iniciando puerto serial nuevamente porque pues ya no tenemos el 	programa anterior\r\n".encode())
	while True:
		print('Por favor introduce un numero a escribir a la mano')
		var = input()	
		print(f'<1.3.1.{var}.{var}.{var}.{var}.{var}.{var}>')
		serial_port.write((f'<1.3.1.{var}.{var}.{var}.{var}.{var}.{var}>').encode())
		print(f'<1.5.1.{var}.{var}.{var}.{var}.{var}.{var}>')
		serial_port.write((f'<1.5.1.{var}.{var}.{var}.{var}.{var}.{var}>').encode())
			


except KeyboardInterrupt:
	print("Exiting Program")

except Exception as exception_error:
	print("Error occurred. Exiting Program")
	print("Error: " + str(exception_error))

finally:
	serial_port.close()
	pass
