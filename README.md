# serversForPy

All pyhton UDP servers for interfacing/debugging (Prometheus project).

server.py listens to UDP messages on a given IP/port and shows the data received + client.
integrate.py receives command strings and sends them through UART protocol. (sudo is mandatory to access serial communication).
decode.py receives commands from the pedals' interface and decodes it to find the STOP signal.
