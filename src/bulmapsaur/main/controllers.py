import jsonpickle
from flask import Flask, Response
from flask import request
from flask_cors import CORS
from flask_sslify import SSLify
import encodeUtils
#from src.bulmapsaur.main.image_recognizer import processImageRecognizer

app = Flask(__name__)
CORS(app)
context = ('src/bulmapsaur/cert/localhost.crt','src/bulmapsaur/cert/localhost.key')
sslify = SSLify(app)

@app.route('/bulmapsaur/api/images', methods=['POST'])
def processImage():
    imageName = request.args.get('name')
    print(request.data)
    img_decoded = base64Decode(request.data)
    # saveImage(img_decoded, imageName)
    img = stringToImage(img_decoded)
#    processImageRecognizer(imageName+".jpg")
    response = {'message': 'image received. size={}x{}'.format(img.shape[0], img.shape[1])}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = '8443',ssl_context = context,debug = True)