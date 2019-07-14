import jsonpickle
import json
from flask import Flask, Response, request
from flask_cors import CORS
from flask_sslify import SSLify

from encodeUtils import (base64Decode, saveImage,
                                             stringToImage)
from image_recognizer import processImageRecognizer

app = Flask(__name__)
CORS(app)
context = ('src/bulmapsaur/cert/selfsigned.crt','src/bulmapsaur/cert/selfsigned.key')
sslify = SSLify(app)

@app.route('/bulmapsaur/api/images', methods=['POST'])
def processImage():
    data = request.data
    imageInfo = json.loads(data)
    imageName = imageInfo.get('name')
    imageB64 = imageInfo.get('base64')
    img_decoded = encodeUtils.base64Decode(imageB64)
    encodeUtils.saveImage(imageName,img_decoded)
    img = encodeUtils.stringToImage(img_decoded)
    encodeUtils.processImageRecognizer(imageName+".jpg")
    response = {'message': 'image received. size={}x{}'.format(img.shape[0], img.shape[1])}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = '8443',ssl_context = context,debug = True)
