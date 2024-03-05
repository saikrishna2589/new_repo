# steps
# start webcam
# detect movement
# capture image
# tell email script to send email with image

# start webcam
import cv2
import time

video=cv2.VideoCapture(0) # if only 1 cam-> place 0 to use that main cam.
#if secondary cam use, then use (1)
time.sleep(1) # this avoids blackframe as it camera
#some time to load


while True:

    check,frame = video.read()
    cv2.imshow("My video", frame)

#creates key board key object
    key=cv2.waitKey(1)

    if key==ord("q"):
        break

video.release()


#you can see the frame captured using 'imshow' method
#but 'imshow' should be used inside a while loop



#frame is the matrix output of one image captured that comes from numpy.
#this is basically list of list of lists
