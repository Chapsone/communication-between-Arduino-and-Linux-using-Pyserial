#!/usr/bin/env python3
import serial 
import time

print("the serial file has been started")
ser = serial.Serial('/dev/ttyACM0', 115200, timeout= 1.0)
time.sleep(3)

ser.reset_input_buffer()

# the void loop
try:
    i = 0
    while True:
        #reception code
        time.sleep(0.01) # to avoid running this file att full speed of Linux or Raspberry
        if ser.in_waiting > 0 : # if serial.available() in Arduino
            line = ser.readline().decode('utf-8') # string reading
            print (line)

        #transmission
        time.sleep(1)
        data = "hello" + str(i)
        ser.write(data.encode('utf-8'))
        ser.write("\n".encode('utf-8'))
        i+=1 
except KeyboardInterrupt:
    print("the serial communication has been closed")
    ser.close()



