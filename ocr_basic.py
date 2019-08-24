#!/usr/bin/python


import cv2
#doesn't import entire library but specific one
from PIL import Image
from pytesseract import image_to_string

#open an image and sets it to a variable
img = Image.open("/Users/Victor/Documents/Github/OCR/test.jpg")
#reads the image into the mat format for cv2 I think
    #not quite sure what mat is
image = cv2.imread("/Users/Victor/Documents/Github/OCR/test.jpg")

#in order to threshold, you must have a grayscale image
#i think in the case of this project, out goal is to simply binarize the image into black and white
#for our early images and tests, we will set a simple value as i mostly want to deal with clearn images
#to learn about image process

#going closer to 0 means changin black pixels to white
#i assume the opposite going the other way
ret, threshold = cv2.threshold(image, 180, 255, cv2.THRESH_BINARY)

text_og = image_to_string(img)
text_threshold = image_to_string(threshold)
#prints text to command console
#will prob change to output file instead at some point
#print(text)

#writes to the file about what it has read/scanned
#"w" makes the file writable
original = open("no_filter.txt", "w")
original.write(text_og)
original.close()

threshold_text = open("threshold_static.txt", "w")
threshold_text.write(text_threshold)
threshold_text.close()

#displays scanned image to the user
cv2.imshow('oringal image',image)
cv2.imshow('threshold 100', threshold)
#waits infinite amount of time for keystroke
cv2.waitKey(0)
#closes image after keystroke
cv2.destroyAllWindows()

#can also save image
#cv2.imwrite('filename.jpg', img)

#this comes later down the line in which we take some statistical value of data from a not so great imgae
#determine the threshold, and binarize based off of that
#this would be a point to bring up with jonny about what type of statistical model we should use
    #or if we really want to go crazy, we do machine learning to determine it


#at some point we might have to take into account the amount of pixels present per image but for
#right now we can ignore

