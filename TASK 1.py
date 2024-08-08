import numpy as np
import cv2 

"""def FrameCapture(path): 
    
    vidObj = cv2.VideoCapture(path) 
     
    count = 0

    success = 1
  
    while success: 
  
        
        success, image = vidObj.read() 
  
        
        cv2.imwrite("frame%d.jpg" % count, image) 
  
        count += 1
   
if __name__ == '__main__': 
  
     
    FrameCapture("C:\\Users\\maila\\OneDrive\\Desktop\\WSPROJECT\\1.mp4")"""
    
cap = cv2.VideoCapture('C:\\Users\\maila\\OneDrive\\Desktop\\WSPROJECT\\1.mp4')
fgbg = cv2.createBackgroundSubtractorKNN()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(1,1))
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    img=cv2.cvtColor(fgmask,cv2.COLOR_BGR2RGB)
    edge=cv2.Canny(img,200,200)
    lines=cv2.HoughLinesP(edge,1,np.pi/180,threshold=10,minLineLength=50,maxLineGap=20)
    print(type(lines))
    """for i in lines:
        x1,x2,y1,y2=i[0]
        cv2.line(fgmask,(x1,x2),(y1,y2),(0,0,255),3)"""
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

