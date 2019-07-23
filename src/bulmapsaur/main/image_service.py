from tornado.log import app_log
import src.bulmapsaur.main.utils.encode_utils as base64Decode
import src.bulmapsaur.main.utils.file_utils as saveImage

from src.bulmapsaur.main.image_analyzer import analyze


async def processImage(imageName,imageB64):
    app_log.info("Processing image %s ...",imageName)
    img_decoded = base64Decode(imageB64)
    saveImage(imageName,img_decoded)
    analyze(imageName+".jpg")
    app_log.info("Image %s succesfully processed ",imageName)
