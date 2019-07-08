import base64
import cv2
import jsonpickle
import numpy as np
from flask import Flask, Response
from flask import request

app = Flask(__name__)

def stringToImage(base64_string):
    decoded_string = base64.b64decode(base64_string)
    np_arr = np.fromstring(decoded_string, np.uint8)
    return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)


@app.route('/notify-new-image', methods=['POST'])
def notifyNewImage():
    #example encode base 64
    #filename = "/home/matiaszeitune/Descargas/hoja.jpg"
    #with open(filename, "rb") as fid:
    #    data = fid.read()

    #b64_bytes = base64.b64encode(data)
    #print(b64_bytes)
    img = stringToImage(request.data)

    response = {'message': 'image received. size={}x{}'.format(img.shape[0], img.shape[1])}

    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


app.run(port=8090)