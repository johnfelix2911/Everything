import cv2
import serial

port_name = 'COM6'  
baud_rate = 9600

ser = serial.Serial(port_name, baud_rate)

cap = None
recording = False
data = None

try:
    while True:
        if ser:
            try:
                if ser.in_waiting > 0:
                    data = ser.readline().decode('utf-8').strip()
                if data == "Motion detected":
                    if not recording:
                        #cap = cv2.VideoCapture(camera_idx)
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
                            cv2.destroyAllWindows()
                
                if recording and cap and cap.isOpened():
                    ret, frame = cap.read()
                    if ret:
                        cv2.imshow("Motion detected", frame)
                        cv2.waitKey(1)
            except Exception as e:
                print(e)
        else:
            print("Serial port is not opened")
except:
    print("Interrupted by user")
    
ser.close()
    
                
