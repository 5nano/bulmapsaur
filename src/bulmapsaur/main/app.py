from tornado.options import define, options
import tornado.ioloop
import tornado.web
import tornado.httpserver
import json
import logging
from logging.config import fileConfig
import os.path

import image_service as imageService

fileConfig('config/logging_config.ini',disable_existing_loggers=False)
logger = logging.getLogger()

class ImageRequestHandler(tornado.web.RequestHandler):
    async def post(self): 
            data = self.request.body
            imageInfo = json.loads(data)
            imageName = imageInfo.get('name')
            imageB64 = imageInfo.get('base64')
            logger.info("Image %s received",imageName)
            #En algun momento va a correr
            tornado.ioloop.IOLoop.current().spawn_callback(imageService.processImage, imageName, imageB64)
            self.write("Ok")
            self.finish()


app = tornado.web.Application([
    (r"/bulmapsaur/api/images", ImageRequestHandler)
    
])

define("port", default="8443", help="Port to listen on")

ssl_ctx = tornado.httpserver.ssl.create_default_context(tornado.httpserver.ssl.Purpose.CLIENT_AUTH)
ssl_ctx.load_cert_chain(os.path.join('src/bulmapsaur/cert/', 'selfsigned.crt'),
                        os.path.join('src/bulmapsaur/cert/', 'selfsigned.key'))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(options.port)
    # autodetect cpu cores and fork one process per core
    try:
        server.start(0)
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()