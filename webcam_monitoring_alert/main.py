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

first_frame=None

while True:

    check,frame = video.read()

    #turning video to grayscale as we dont really need Blue,red,green combintations in video to compare motion
    grayframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #another transformation to make calculation more efficient .grayframe will be blurred a bit amd removes noise.
   # (21,21) is amount of blurredness we want to give and 0 is the standard dev
    gray_frame_gau=cv2.GaussianBlur(grayframe,(21,21),0)


    if first_frame is None:
        first_frame=gray_frame_gau
        #taking difference between first frame and latest frame to detect motion and altert
    delta_frame=cv2.absdiff(first_frame,gray_frame_gau)


    #classifying the pixel-->white in pixel would be cloe to 255 in the frame. close to 0 will be black
    #we compare to first value when it is all black and then compare with following frames
    #
    thresh_frame= cv2.threshold(delta_frame,45,255,cv2.THRESH_BINARY)[1]
    dil_frame=cv2.dilate(thresh_frame,None,iterations=2)
    cv2.imshow("My video", dil_frame)

    contours,check=

    #print(thresh_frame)
    #if you print(delta_frame) , we get closer to 0 values if you are outside the camera ,which means closer to black
    #color. but as you as someone comes int th camera delta frame values jump to 40-50 etc,closer to white pixel

    #creates key board key object
    key=cv2.waitKey(1)

    if key==ord("q"):
        break

video.release()


#you can see the frame captured using 'imshow' method
#but 'imshow' should be used inside a while loop



#frame is the matrix output of one image captured that comes from numpy.
#this is basically list of list of lists
