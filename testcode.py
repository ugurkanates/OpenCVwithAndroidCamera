import urllib.request
import cv2
import numpy as np
# Replace the URL with your own IPwebcam shot.jpg IP:port
url="http://192.168.1.146:8080/"

cv2.namedWindow('window_frame')

ANDROID_DEVICE = True
ANDROID_AS_VIDEO = True

URL= "http://192.168.1.146:8080/video?type=some.mjpeg"
video_capture = cv2.VideoCapture(URL)
process_this_frame = True
USE_SMALL_FRAME = True

while True:

    if(ANDROID_DEVICE == True and ANDROID_AS_VIDEO == False):
            # Use urllib to get the image from the IP camera
        imgResponse = urllib.request.urlopen(url)

        # Numpy to convert into a array
        imgNp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)

        # Decode the array to OpenCV usable format
        img = cv2.imdecode(imgNp,-1)
        bgr_image = img
    elif(ANDROID_DEVICE == True and ANDROID_AS_VIDEO == True):
        bgr_image = video_capture.read()[1]
    else:
        bgr_image = video_capture.read()[1]

        
    if process_this_frame:
        gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
        rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
        
        if USE_SMALL_FRAME:
            rgb_image = cv2.resize(rgb_image, (0, 0), fx=0.25, fy=0.25)
        
        #result_img = face.detect_face(rgb_image)
        
        if USE_SMALL_FRAME:
            rgb_image = cv2.resize(rgb_image, (0, 0), fx=2, fy=2)
        
        bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
        cv2.imshow('window_frame', bgr_image)
        
    process_this_frame = not process_this_frame
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
video_capture.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
