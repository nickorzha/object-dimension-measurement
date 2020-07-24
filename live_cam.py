import urllib.request
import cv2
import numpy as np
import os


# Replace the URL with your own IPwebcam shot.jpg IP:port
url=f"http://{os.environ.get('MOBILE_IP')}/shot.jpg"

def live():

    # Use urllib to get the image and convert into a cv2 usable format
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)

    return img
