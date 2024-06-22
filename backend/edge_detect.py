import cv2

def detect(img_dir):
    img = cv2.imread(img_dir)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 100, 200)

    return canny