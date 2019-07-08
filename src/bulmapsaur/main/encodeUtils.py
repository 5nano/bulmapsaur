import base64
import cv2
import numpy as np


def base64Decode(base64_string):
    return base64.b64decode(base64_string)

def stringToImage(decoded_string):
    np_arr = np.fromstring(decoded_string, np.uint8)
    return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

def imageToBase64(): #just to see how it is a base 64
    filename = "/home/matiaszeitune/Descargas/hoja.jpg"
    with open(filename, "rb") as fid:
        data = fid.read()
    #example encode base 64
    b64_bytes = base64.b64encode(data)
    print(b64_bytes)

def saveImage(img,name):
    filename = name+'.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(img)