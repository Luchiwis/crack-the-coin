import serial
import serial.tools.list_ports
import time



def dropcoin():
    for arduino_port in list(serial.tools.list_ports.comports()):
        if arduino_port.device != 'COM1':
            print('Arduino is connected')
            ser = serial.Serial(arduino_port.device, 9600)
            time.sleep(2)

            ser.write("1".encode())
            print("Coin dropped")
            
            ser.close()
    
    

if __name__ == "__main__":
    dropcoin()