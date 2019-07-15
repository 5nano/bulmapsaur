import logging
from logging.config import fileConfig

import image_analyzer as imageAnalyzer
import utils.encode_utils as encodeUtils
import utils.file_utils as fileUtils

fileConfig('config/logging_config.ini',disable_existing_loggers=False)
logger = logging.getLogger()


async def processImage(imageName,imageB64):
    logger.info("Processing image %s ...",imageName)
    img_decoded = encodeUtils.base64Decode(imageB64)
    fileUtils.saveImage(imageName,img_decoded)
    #imageAnalyzer.analyze(imageName+".jpg")
    logger.info("Image %s succesfully processed ",imageName)
