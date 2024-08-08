import numpy as np
import cv2
import keyboard as kb
import math
import random
import os

x=250
y=250
speed=5
angle=0
start_angle=40
end_angle=320
prev_start_angle=start_angle+1
c=0
r1=50
r2=80
r=10
p=0
q=100
d=0
n=348
flag=0

def game_over():
    message = "GAME OVER"
    font_size = 2
    font_color = (0, 0, 255)
    img = np.zeros((500, 500, 3), dtype=np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size, baseline = cv2.getTextSize(message, font, font_size, 2)
    text_center_x = int((img.shape[1] - text_size[0]) / 2)
    text_center_y = int((img.shape[0] + text_size[1]) / 2)
    cv2.putText(img, message, (text_center_x, text_center_y - baseline), font, font_size, font_color, 2)
    cv2.imshow("pac",img)
    cv2.waitKey(3000)
    message = "SCORE:"+str(r)
    font_size = 2
    font_color = (0, 0, 255)
    img = np.zeros((500, 500, 3), dtype=np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size, baseline = cv2.getTextSize(message, font, font_size, 2)
    text_center_x = int((img.shape[1] - text_size[0]) / 2)
    text_center_y = int((img.shape[0] + text_size[1]) / 2)
    cv2.putText(img, message, (text_center_x, text_center_y - baseline), font, font_size, font_color, 2)
    cv2.imshow("pac",img)
    cv2.waitKey(3000)
    os._exit(0)

a=random.randint(10,490)
b=random.randint(10,490)

while True:
    img=np.full((500,500,3),(0,0,0),dtype=np.uint8)
    cv2.ellipse(img,(x,y),(r,r),angle,start_angle,end_angle,(0,0,255),-1) #pacman
    cv2.ellipse(img,(a,b),(5,5),0,0,360,(0,255,0),-1) #food
    if p%500==0:
        p=0
    p=p+5
    cv2.ellipse(img,(p,q),(15,15),0,0,360,(0,255,255),-1) #linear motion obstacle
    c=c+1
    if kb.is_pressed('w'):
        if y>10:
            y=y-speed
        angle=270
    if kb.is_pressed('s'):
        if y<490:
            y=y+speed
        angle=90
    if kb.is_pressed('a'):
        if x>10:
            x=x-speed
        angle=180
    if kb.is_pressed('d'):
        if x<490:
            x=x+speed
        angle=0
    if (c//20)%2==0:
        start_angle=40
        end_angle=320
    else:
        start_angle=5
        end_angle=355
    m1=math.floor((500+math.sqrt(250000-4*(n*n-500*n+102500)))/2)
    m2=math.floor((500-math.sqrt(250000-4*(n*n-500*n+102500)))/2)
    cv2.ellipse(img,(m1,n),(r1,r1),0,0,360,(0,255,255),3) #circular motion obstacle
    cv2.ellipse(img,(m2,n),(r1,r1),0,0,360,(0,255,255),3) #circular motion obstacle
    if n==100:
        flag=1
    if n==400:
        flag=0
    if flag==0:
        n=n-2
    else:
        n=n+2
    if (r+5)>math.sqrt((x-a)*(x-a)+(y-b)*(y-b)):
        a=random.randint(10,490)
        b=random.randint(10,490)
        r=r+2
    if (r1+r)>math.sqrt((x-m1)*(x-m1)+(y-n)*(y-n)) or (r1+r)>math.sqrt((x-m2)*(x-m2)+(y-n)*(y-n)) or (15+r)>math.sqrt((x-p)*(x-p)+(y-q)*(y-q)):
        game_over()
    cv2.imshow("pac",img)
    if cv2.waitKey(10)==ord("q"):
        break
cv2.destroyAllWindows()