import numpy as np
import cv2

img = cv2.imread("map_final.jpg")
img = cv2.resize(img, (800,500))
#map = np.full((800,500,3), (255,255,255), dtype = np.uint8)

cv2.imshow("hehe", img)
cv2.waitKey(0)
lis = []

lis.append([img[0][0][0], img[0][0][1], img[0][0][2]])

y = 0
for i in img:
    x = 0
    for j in i:
        l = [j[0], j[1], j[2]]
        if (l not in lis):
            if j[1]<100 and j[2]<100:
                img = cv2.imread("final_proj_img.jpg")
                img = cv2.resize(img, (800,500))
                #map[y][x][1] = 0
                #map[y][x][2] = 0
                lis.append(l)
                print(l)
                image = np.full((500,500,3), (l[0],l[1],l[2]), dtype = np.uint8)
                cv2.ellipse(img, (x,y), (15,15), 0, 0, 360, (0,0,255), 3)
                cv2.imshow("map2", img)
                #cv2.imshow("map", map)
                cv2.imshow("color", image)
                cv2.waitKey(800)
            else:
                img[y][x][0] = 255
                img[y][x][1] = 255
                img[y][x][2] = 255
                print("Erasing")
        x = x + 1
    y = y + 1

cv2.destroyAllWindows()