import cv2
import numpy as np

def generator(img_dir):
    # Read in image
    img = cv2.imread(img_dir, 0)
    img = 255 - img
    img = cv2.resize(img, (6000,6000))
    h,w = img.shape
    cutter_size = 20
    buffer = int(cutter_size * 1.25)
    img2 = np.zeros((h+buffer*2, w+buffer*2), np.uint8)
    img2[buffer:buffer+h, buffer:buffer+w] = img
    img = img2.copy()

    h,w = img.shape

    # Define parameters
    pixels_to_inch = 1000
    depth_per_cut = 125 # Value in thousands
    depth = 500 # Value in thousands
    jog_speed = "15"
    feed_speed = "9"
    plunge_speed = "3"
    current_depth = 0
    cuts = 2

    # Find the center of the part - there should only be one contour
    contours, _ = cv2.findContours(img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contour = contours[1]

    kernel = np.ones((20,20), np.uint8)
    dilate = cv2.dilate(img, kernel, iterations = 4)

    contours_dilate = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour_dilate = contours_dilate[0]

    # Change the contours from arrays to lists
    outter = []
    for point in contour_dilate[0]:
        outter.append(tuple(point[0]))
    inner = []
    for point in contour:
        inner.append(tuple(point[0]))

    h,w = img.shape
    bg = np.zeros((h,w,3), np.uint8)
    bg = img.copy()
    bg = cv2.drawContours(bg, [contour], -1, (255,255,0), 2)
    bg = cv2.drawContours(bg, contour_dilate, -1, (0,0,255), 2)
    # cv2.imshow('img', cv2.resize(bg, (987,987)))
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    bg = np.zeros((h,w,3), np.uint8)
    for i in range(len(inner)-1):
        a = inner[i]
        b = inner[i-1]
        cv2.line(bg, a, b, (0,255,0), cutter_size)
    for i in range(len(outter)-1):
        a = outter[i]
        b = outter[i+1]
        cv2.line(bg, a, b, (255,0,255), cutter_size)
        
    bg = cv2.drawContours(bg, [contour], -1, (255,255,0), 2)
    bg = cv2.drawContours(bg, contour_dilate, -1, (0,0,255), 2)
    # cv2.imshow('img', cv2.resize(bg, (987,987)))
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    # Create string for g_code
    g_code = "%" + "\n"
    g_code += "G64 P0.001" + "\n"
    g_code += "M6 T1" + "\n"
    g_code += "M3 S5000" + "\n"
    g_code += "G1 F" + jog_speed + "\n"
    g_code += "G1X0.0000Y0.0000Z0.1000" + "\n"
    g_code += "G1 F" + jog_speed + "\n"

    # Jog to the first point in the contour
    dilate_origin = tuple(contour_dilate[0][0][0])
    g_code += "G1 X" + str(dilate_origin[0]/1000.00) + "Y" + str(dilate_origin[1]/1000.00) + "\n"

    origin = tuple(contour[0][0])

    previous_point = dilate_origin

    # Change the contours from arrays to lists
    outter = []
    for point in contour_dilate[0]:
        outter.append(tuple(point[0]))
    inner = []
    for point in contour:
        inner.append(tuple(point[0]))

    # Make cuts
    for cut in range(cuts):
        # Plunge into the material
        g_code += "G1 F" + plunge_speed + "\n"
        current_depth -= depth_per_cut
        g_code += "G1 Z" + str(current_depth/1000.00) + "\n"

        # Cut the bigger contour
        g_code += "G1 F" + feed_speed + "\n"

        # Iterate through each point in the dilated contour
        for point in outter:
            x = point[0]/1000.00
            y = point[1]/1000.00
            g_code += "X" + str(x) + "Y" + str(y) + "\n"

        
        # Go back to the origin
        g_code += "G1 X" + str(dilate_origin[0]/1000.00) + "Y" + str(dilate_origin[1]/1000.00) + "\n"
                
        # Iterate through each point in the contour
        for point in inner:
            x = point[0]/1000.00
            y = point[1]/1000.00
            g_code += "X" + str(x) + "Y" + str(y) + "\n"
                
        # Go back to the origin
        g_code += "G1 X" + str(origin[0]/1000.00) + "Y" + str(origin[1]/1000.00) + "\n"
    g_code += "G0Z.1"
    g_code += "M5\n"
    g_code += "M02\n"
    g_code += "%"

    # print(g_code)
    return g_code

# # Test Code
# img_dir = '/Users/crossrunway/Downloads/gt3.jpeg'
# print(gcode_generator(img_dir))