import cv2      #OpenCV
import serial   #PySerial

port_name = 'COM6'  
baud_rate = 9600    #Speed of data transfer

ser = serial.Serial(port_name, baud_rate)    #Initializing Serial object

cap = None
recording = False
data = None

try:
    while True:    #Infinite loop
        if ser:    #Check if serial port is opened
            try:
                if ser.in_waiting > 0: # Checks if there is data to be read from serial port
                    data = ser.readline().decode('utf-8').strip()   #Read a whole line of data
                if data == "Motion detected":
                    if True:
                        cap = cv2.VideoCapture(1)   #It will start capturing the video from external webcam
                        #Inbuilt camera has the index 0        #External camera has the index 1.
                        if cap.isOpened():          #To check if the camera is opened
                            recording = True        #We set the variable 'recording' to True because the recording is started 
                        else:
                            print("Error opening camera")
                elif data == "No motion":
                    if recording:              #We check if the recording is going on or not
                        recording = False      #If the recording is going on we set 'recording' to false
                        if cap:                #We check if the camera is open
                            cap.release()      #We stop capturing the video
                            cv2.destroyAllWindows()         #We close the video window
                
                if recording and cap and cap.isOpened():    #and - it checks for truth value of all the statements and only if all statements are true the entire statement becomes true
                    ret, frame = cap.read()              #To read the frames from camera
                    if ret:
                        cv2.imshow("Motion detected", frame)     #To display the recorded frame on a new window
                        cv2.waitKey(1)           #we wait for a key to be pressed for 1 millisecond
            except Exception as e:         #Exception = Error
                print(e)
        else:
            print("Serial port is not opened")
except:              #This is executed if there is an exception (error) in the try block
    print("Interrupted by user")
    
ser.close()           #We have to close the serial port 
