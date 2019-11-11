import json
import os.path
import os
from tornado.log import app_log
from datetime import datetime
import tornado.ioloop
import tornado.web
from tornado.httpserver import HTTPServer, ssl
from tornado.ioloop import IOLoop
from tornado.options import define, options

import image_service as imageService

class ImageRequestHandler(tornado.web.RequestHandler):
    async def post(self): 
            data = self.request.body
            imageInfo = json.loads(data)
            idAssay = imageInfo.get('idAssay')
            idExperiment = imageInfo.get('idExperiment')
            optionalTime = None
            if imageInfo.get('optionalTime') is not None:
                optionalTime = imageInfo.get('optionalTime')
            imageB64 = imageInfo.get('base64')
            app_log.info("Image with idAssay %s and idExperiment %s received",idAssay,idExperiment)
            #En algun momento va a correr
            IOLoop.current().spawn_callback(imageService.processImage, idAssay,idExperiment, imageB64, optionalTime)
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
    server = HTTPServer(app)
    server.bind(options.port)
    # autodetect cpu cores and fork one process per core
    try:
        server.start(0)
        IOLoop.instance().start()
    except KeyboardInterrupt:
        IOLoop.instance().stop()
