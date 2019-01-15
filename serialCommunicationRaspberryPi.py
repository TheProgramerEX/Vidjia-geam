import serial, time

arduinoSerialData1 = serial.Serial('/dev/ttyUSB0', 9600)
arduinoSerialData2 = serial.Serial('/dev/ttyUSB1', 9600)
arduinoSerialData3 = serial.Serial('/dev/ttyUSB2', 9600)
time.sleep(1)
arduinoSerialData1.flushInput()
arduinoSerialData2.flushInput()
arduinoSerialData3.flushInput()
arduinoSerialData1.write(bytes('Hello World', 'UTF-8'))
arduinoSerialData2.write(bytes('Yes', 'UTF-8'))
arduinoSerialData3.write(bytes('GoodBye', 'UTF-8'))
i = 0
while (i< 13):
    arduinoSerialData1.write(bytes('Hello World', 'UTF-8'))
    arduinoSerialData2.write(bytes('Yes', 'UTF-8'))
    arduinoSerialData3.write(bytes('Goodbye', 'UTF-8'))
    time.sleep(.5)
    print (i)
    i = i + 1
print ("All finished")



