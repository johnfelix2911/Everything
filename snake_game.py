import cv2
import keyboard as kb
import numpy as np

def grid():
    img = np.full((600, 600), 0, dtype = np.uint8)
    cv2.imshow("grid", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    for i in range(59):
        cv2.line(img, (0, (i + 1)*10), (599, (i + 1)*10), (255, 255, 255), 1)
        cv2.line(img, ((i + 1)*10, 0), ((i + 1)*10, 599), (255, 255, 255), 1)
    cv2.imshow("grid", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

grid()
body = []
head = [295, 295]
tail = [285, 295]
while True:
    if kb.is_pressed('q'):
        break
    if kb.is_pressed('w'):
        head[1] = head[1] - 10
    if kb.is_pressed('s'):
        head[1] = head[1] + 10
    if kb.is_pressed('a'):
        head[0] = head[0] - 10
    if kb.is_pressed('d'):
        head[0] = head[0] + 10
    