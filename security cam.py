import cv2
import serial

port_name = 'COM6'  
baud_rate = 9600

ser = serial.Serial(port_name, baud_rate)

cap = None
recording = False

try:
    while True:
        if ser:
            try:
                data = ser.readline().decode('utf-8').strip()
                if data == "Motion detected":
                    if not recording:
                        cap = cv2.VideoCapture(0)
                        if cap.isOpened():
                            recording = True
                        else:
                            print("Error opening camera")
                elif data == "No motion":
                    if recording:
                        recording = False
                        if cap:
                            cap.release()
                else:
                    continue
                
                if recording and cap and cap.isOpened():
                    ret, frame = cap.read()
                    if ret:
                        cv2.imshow("Recording", frame)  
            except:
                print("Error reading from serial port")
        else:
            print("Serial port is not opened")
except:
    print("Interrupted by user")
    
finally:
    if ser and ser.is_open:
        ser.close()
    if cap and cap.isOpened():
        cap.release()
    cv2.destroyAllWindows()
                
