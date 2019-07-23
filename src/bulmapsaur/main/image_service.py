from tornado.log import app_log
from utils.encode_utils import base64Decode
from utils.file_utils import saveImage

from image_analyzer import analyze


async def processImage(imageName,imageB64):
    app_log.info("Processing image %s ...",imageName)
    img_decoded = base64Decode(imageB64)
    saveImage(imageName,img_decoded)
    analyze(imageName+".jpg")
    app_log.info("Image %s succesfully processed ",imageName)
