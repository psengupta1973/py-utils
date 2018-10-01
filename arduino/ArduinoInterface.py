import time
import serial

class ArduinoInterface:

    def __init__(self, port, rate=9600):
        self.arduino = serial.Serial(port, rate)
        time.sleep(2) #waiting the initialization...

    def setLed(self, command):
        #command = input("Type something..: (on/ off / bye )")
        if command =="on":
            print("The LED is on...")
            time.sleep(1) 
            self.arduino.write(b'H') 
            #setLed()
        elif command =="off":
            print("The LED is off...")
            time.sleep(1) 
            self.arduino.write(b'L')
            #setLed()
        elif command =="bye":
            print("See You!...")
            self.arduino.write(b'B')
            time.sleep(1) 
            self.arduino.close()
        else:
            print("ERROR: Sorry..invalid LED command..!")
            #setLed()

def test(times=5):
    ard = ArduinoInterface('COM3')
    for i in range(0, times):
        ard.setLed('on')
        ard.setLed('off')
    ard.setLed('bye')

#test()