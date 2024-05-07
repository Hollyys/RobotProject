import cv2

img_dir = '/Users/crossrunway/Downloads'
img = cv2.imread(img_dir)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

g_code = ""
for contour in contours:
    for point in contour:
        x, y = point[0]
        g_code += "G01 X{} Y{}\n".format(x, y)

print(g_code)
