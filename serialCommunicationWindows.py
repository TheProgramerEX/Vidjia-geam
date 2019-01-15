import serial, time

arduinoSerialData1 = serial.Serial('COM4', 9600)

time.sleep(1)
arduinoSerialData1.flushInput()

arduinoSerialData1.write(bytes('Hello World', 'UTF-8'))

i = 0
while (i< 13):
    arduinoSerialData1.write(bytes('Hello World', 'UTF-8'))

    time.sleep(.5)
    print (i)
    i = i + 1
print ("All finished")



