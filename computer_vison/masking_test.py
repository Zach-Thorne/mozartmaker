import cv2
import matplotlib.pyplot as plt
import numpy as np
import time

# FUNCTION TO CREATE MASK --> WILL isolate the white keys
#TODO Make it so that this takes image as argument
def create_mask(): 
    print("Create mask over image for test. Isolate the white keys.") 

    #Read image in as RGB
    image = cv2.imread("test2_img.jpg")
    image = cv2.imread("test2_img.jpg")

    #Resize image so it is nice to deal with 
    image = cv2.resize(image, (960, 540))

    #Print image size for finr
    print("Image size" + str(image.shape) + "\n")
    cv2.imshow("Original", image) 
    # Convert BGR to HSV
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Image size" + str(gray.shape) + "\n")
    # Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #Now to isolate white of the keys 
    #NOTE trying with both HSV img and GRAY scale img

    #Trying to create mask in HSV 
    upper_mask_hsv = np.array([0,0,255])   
    lower_mask_hsv = np.array([0,0,204])
    hsv_mask = cv2.inRange(hsv, lower_mask_hsv, upper_mask_hsv)

    #Trying to create mask in HSV 
    upper_mask_gray = np.array(255)   
    lower_mask_gray = np.array(180) #May need to change 
    gray_mask = cv2.inRange(gray, lower_mask_gray, upper_mask_gray)

    #AND matrices to isloate keys
    hsv_res = cv2.bitwise_and(image,image, mask=hsv_mask)
    gray_res = cv2.bitwise_and(image,image, mask=gray_mask)

    cv2.imshow("Original", image) 
    cv2.imshow("gray", gray) 
    cv2.imshow("hsv", hsv) 
    cv2.imshow("hsv mask", hsv_mask) 
    cv2.imshow("gray mask", gray_mask) 
    cv2.imshow("gray_hsv", gray_res) 
    cv2.waitKey(0) # waits until a key is pressed

def create_mask_live(): 
    print("Create mask over live image capture from webcam for test. Isolate the white keys.") 

    #Should capture from webcam
    cap = cv2.VideoCapture(0)
    time.sleep(2)

    while(1):
        #Take each frame
        _, frame = cap.read()

        # Convert BGR to Gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print("Image size" + str(gray.shape) + "\n")
        # Convert BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        #Now to isolate white of the keys 
        #NOTE trying with both HSV img and GRAY scale img

        #Trying to create mask in HSV 
        upper_mask_hsv = np.array([0,0,255])   
        lower_mask_hsv = np.array([0,0,204])
        hsv_mask = cv2.inRange(hsv, lower_mask_hsv, upper_mask_hsv)

        #Trying to create mask in HSV 
        upper_mask_gray = np.array(255)   
        lower_mask_gray = np.array(180) #May need to change 
        gray_mask = cv2.inRange(gray, lower_mask_gray, upper_mask_gray)

        #AND matrices to isloate keys
        hsv_res = cv2.bitwise_and(frame,frame, mask=hsv_mask)
        gray_res = cv2.bitwise_and(frame,frame, mask=gray_mask)

        cv2.imshow("Original", frame) 
        cv2.imshow("gray", gray) 
        cv2.imshow("hsv", hsv) 
        cv2.imshow("hsv mask", hsv_mask) 
        cv2.imshow("gray mask", gray_mask) 
        cv2.imshow("gray_hsv", gray_res) 
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            break

create_mask() 
cv2.destroyAllWindows() # destroys the window showing image
