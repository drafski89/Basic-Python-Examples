import serial

# nameOfPort = serial.Serial(which serial port number to open)
serialPort = serial.Serial(0)
# set the serialPort baud rate
serialPort.baudrate = 115200

# read a line from serialPort
print serialPort.readline()

# close the serial port
serialPort.close()