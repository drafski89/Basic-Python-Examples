import serial

ser = serial.Serial(0)
ser.baudrate = 115200

while True:
	print ser.readline().strip()