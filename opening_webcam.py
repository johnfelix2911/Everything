import cv2

for camera_idx in range(1, 10):
    cap = cv2.VideoCapture(camera_idx)
    if cap.isOpened():
        print("Camera found at index:", camera_idx)
        cap.release()
        break

cap = cv2.VideoCapture(camera_idx)
if not cap.isOpened():
    print("Error opening webcam")
    exit()

while True:
    _, frame = cap.read()
    
    if not _:
        print("Failed to capture frame")
        break

    cv2.imshow("External_Webcam", frame)
    k = cv2.waitKey(1)
    if k == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()