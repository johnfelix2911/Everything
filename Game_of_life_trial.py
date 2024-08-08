import cv2
import numpy as np
import keyboard as kb

img = np.full((500,500,3), (0,0,0), dtype = np.uint8)
for i in range(49):
    cv2.line(img, (0, (i+1)*10), (499, (i+1)*10), (255,255,255), 1)
    cv2.line(img, ((i+1)*10, 0), ((i+1)*10, 499), (255,255,255), 1)
cv2.imshow("hehe", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

x = 0
y = 0
live = []
cv2.rectangle(img, (x,y),(x+10,y+10), (0,0,255), 2)
cv2.imshow("hehe", img)
while (1):
    cv2.rectangle(img, (x,y), (x+10,y+10), (0,0,0), 2)
    cv2.rectangle(img, (x,y), (x+10,y+10), (255,255,255), 1)
    if kb.is_pressed('w'):
        if (y>0):
            y = y - 10
    if kb.is_pressed('s'):
        if (y<490):
            y = y + 10
    if kb.is_pressed('d'):
        if (x<490):
            x = x + 10
    if kb.is_pressed('a'):
        if (x>0):
            x = x - 10
    if kb.is_pressed('q'):
        break
    if kb.is_pressed('j'):
        cv2.rectangle(img, (x,y), (x+10,y+10), (255,255,255), -1)
        live.append((x+5,y+5))
    cv2.rectangle(img, (x,y),(x+10,y+10), (0,0,255), 2)
    cv2.imshow("hehe", img)
    cv2.waitKey(50)

for i in range(49):
    cv2.line(img, (0, (i+1)*10), (499, (i+1)*10), (255,255,255), 1)
    cv2.line(img, ((i+1)*10, 0), ((i+1)*10, 499), (255,255,255), 1)
cv2.imshow("hehe", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(live)

grid = []
y = 0
for i in range(49):
    x = 0
    for j in range(49):
        grid.append((x+5,y+5))
        x = x + 10
    y = y + 10

# print(grid)

edge = []
for i in range(50):
    edge.append((5, i*10 + 5))
    edge.append((495, i*10 + 5))
for i in range(50):
    edge.append((i*10 + 5, 5))
    edge.append((i*10 + 5, 495))

next_live = []
while (1):
    for i in grid:
        if i not in edge:
            live_neighbour = 0
            if (i[0], i[1]+10) in live:
                live_neighbour = live_neighbour + 1
            if (i[0], i[1]-10) in live:
                live_neighbour = live_neighbour + 1
            if (i[0]+10, i[1]) in live:
                live_neighbour = live_neighbour + 1
            if (i[0]-10, i[1]) in live:
                live_neighbour = live_neighbour + 1
            if (i[0]+10, i[1]+10) in live:
                live_neighbour = live_neighbour + 1
            if (i[0]+10, i[1]-10) in live:
                live_neighbour = live_neighbour + 1
            if (i[0]-10, i[1]-10) in live:
                live_neighbour = live_neighbour + 1
            if (i[0]-10, i[1]+10) in live:
                live_neighbour = live_neighbour + 1
            #print("live_neighbour=",live_neighbour)
            if i not in live:
                if (live_neighbour==3):
                    next_live.append(i)
                    cv2.rectangle(img, (i[0]-5, i[1]-5), (i[0]+5, i[1]+5), (255,255,255), -1)
            else:
                if (live_neighbour==2 or live_neighbour==3):
                    next_live.append(i)
                    cv2.rectangle(img, (i[0]-5, i[1]-5), (i[0]+5, i[1]+5), (255,255,255), -1)
                else:
                    cv2.rectangle(img, (i[0]-5, i[1]-5), (i[0]+5, i[1]+5), (0,0,0), -1)
    for i in range(49):
        cv2.line(img, (0, (i+1)*10), (499, (i+1)*10), (255,255,255), 1)
        cv2.line(img, ((i+1)*10, 0), ((i+1)*10, 499), (255,255,255), 1)
    live = next_live.copy()
    next_live = []
    cv2.imshow("hehe", img)
    cv2.waitKey(100)
    #print("hello")