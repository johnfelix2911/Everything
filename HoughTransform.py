import cv2
import numpy as np

vid = cv2.VideoCapture("test_video.mp4")
if(vid.isOpened() is False):
    print("Error opening file")
while(vid.isOpened()):
    ret, frame=vid.read()
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    edge=cv2.Canny(img,170,200)
    lines=cv2.HoughLinesP(edge,1,np.pi/180,threshold=100,minLineLength=300,maxLineGap=60)
    print(lines.shape)
    for i in lines:
        x1,x2,y1,y2=i[0]
        cv2.line(frame,(x1,x2),(y1,y2),(0,255,0),3)
    if ret:
        cv2.imshow("Frame",frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
vid.release()
cv2.destroyAllWindows()