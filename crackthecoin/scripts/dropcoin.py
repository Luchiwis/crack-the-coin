import serial
import serial.tools.list_ports
import time



def dropcoin():
    arduino_port = list(serial.tools.list_ports.comports())[0]
    if arduino_port.device != 'COM1':
        print('Arduino is connected')
    else:
        print('ERROR: Arduino is NOT connected')
        return False
    
    ser = serial.Serial(arduino_port.device, 9600)
    time.sleep(2)

    ser.write("1".encode())
    print("Coin dropped")
    
    ser.close()

if __name__ == "__main__":
    dropcoin()