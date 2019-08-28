import json
import os.path
import datetime
from tornado.log import app_log

import tornado.ioloop
import tornado.web
from tornado.httpserver import HTTPServer, ssl
from tornado.ioloop import IOLoop
from tornado.options import define, options

import image_service as imageService

def buildImgName(idTest, idPlant):
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
    imageName = idTest + "-" + idPlant + "-" + dt_string + ".jpg"
    return imageName


class ImageRequestHandler(tornado.web.RequestHandler):
    async def post(self):
        data = self.request.body
        imageInfo = json.loads(data)
        idTest = imageInfo.get('idTest')
        idPlant = imageInfo.get('idPlant')
        imageB64 = imageInfo.get('base64')
        app_log.info(
            "Image with idTest %s and idPlant %s received", idTest, idPlant)
        imageName = buildImgName(idTest, idPlant)
        # En algun momento va a correr
        IOLoop.current().spawn_callback(imageService.processImage, imageName, imageB64)
        self.write("Ok")
        self.finish()


app = tornado.web.Application([
    (r"/bulmapsaur/api/images", ImageRequestHandler)
])

define("port", default="8443", help="Port to listen on")

ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_ctx.load_cert_chain(os.path.join(os.path.dirname(__file__), '../cert/selfsigned.crt'),
                        os.path.join(os.path.dirname(__file__), '../cert/selfsigned.key'))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    server = HTTPServer(app, ssl_options=ssl_ctx)
    server.bind(options.port)
    try:
        server.start(4)
        IOLoop.instance().start()
    except KeyboardInterrupt:
        IOLoop.instance().stop()
