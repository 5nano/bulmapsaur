import base64
import cv2
import numpy as np

def base64Decode(base64_string):
    return base64.b64decode(base64_string)

def base64encode(pathImage):
    with open(pathImage, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    return encoded_string

def stringToImage(decoded_string):
    np_arr = np.fromstring(decoded_string, np.uint8)
    return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)