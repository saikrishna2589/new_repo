import cv2  #open cv library does image proessing, can capture video, process video
# (making them grayscale, blurring)
# it works on pixels of image . video is also made of image

array=cv2.imread("image.png")  #imread method of open cv means imageread.image is the input
print(array.shape)
print(array)

print(type(array))-#<class 'numpy.ndarray'>
#this image is stored as numpy array so heavy numbers can be stored in lists = as arrays.

#shape is 3,4,3 means
