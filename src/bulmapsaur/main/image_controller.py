import asyncio
import json

import jsonpickle
from flask import Flask, Response, request
from flask_cors import CORS
from flask_sslify import SSLify
from threading import Thread

import image_service as imageService

app = Flask(__name__)
CORS(app)
context = ('src/bulmapsaur/cert/selfsigned.crt','src/bulmapsaur/cert/selfsigned.key')
sslify = SSLify(app)

def start_background_loop(loop: asyncio.AbstractEventLoop) -> None:
    asyncio.set_event_loop(loop)
    loop.run_forever()


@app.route('/bulmapsaur/api/images', methods=['POST'])
def processImage():
    loop = asyncio.new_event_loop()
    t = Thread(target=start_background_loop, args=(loop,), daemon=True)
    t.start()    
    data = request.data
    imageInfo = json.loads(data)
    imageName = imageInfo.get('name')
    imageB64 = imageInfo.get('base64')
    #En algun momento va a correr
    asyncio.run_coroutine_threadsafe(imageService.processImage(imageName,imageB64), loop)
    return Response(response=jsonpickle.encode({'message': 'image received'}), status=200, mimetype="application/json")

if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = '8443',ssl_context = context,debug = True)
