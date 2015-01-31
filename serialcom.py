import serial

"""
 The place where the serial magic happens. Please use those pre-defined methods in order to
 communicate with your arduino since you have to set DTR to false. ALWAYS!
"""


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