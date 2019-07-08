import jsonpickle
from flask import Flask, Response
from flask import request

from src.bulmapsaur.main.encodeUtils import stringToImage, saveImage, base64Decode
from src.bulmapsaur.main.image_recognizer import processImageRecognizer

app = Flask(__name__)

@app.route('/bulmapsaur/api/images', methods=['POST'])
def processImage():
    imageName = request.args.get('name')
    img_decoded = base64Decode(request.data)
    saveImage(img_decoded, imageName)
    img = stringToImage(img_decoded)
    processImageRecognizer(imageName+".jpg")
    response = {'message': 'image received. size={}x{}'.format(img.shape[0], img.shape[1])}
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")


app.run(port=8090)