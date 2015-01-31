import serial


def send(port, baud, command):
    com = serial.Serial()
    com.port = port
    com.baudrate = baud
    com.timeout = 1
    com.setDTR(False)
    com.open()
    com.write(command)
    com.close()


def readline(port, baud):
    com = serial.Serial()
    com.port = port
    com.baudrate = baud
    com.timeout = 1
    com.setDTR(False)
    com.open()
    com.readline()