# serversForPy

All pyhton UDP servers for interfacing/debugging (Prometheus project).

## socketServer.py (main):
### (UPDATE!!!! It looks for a specific command to discriminate a STOP signal among actuator commands).
listens to UDP messages on a given IP/port and shows the data received + client. 

## serversForPy/integrate.py (main):
receives command strings and sends them through UART protocol. (sudo is mandatory to access serial communication).

## serversForPy/integrate.py (master):
receives command strings and sends them through UART protocol. (sudo is mandatory to access serial communication).


