from tornado.log import app_log
from utils.encode_utils import base64Decode
from utils.file_utils import saveImage
import os

#from image_analyzer import analyze
from plantcv_service import analyze
from cassandra_connector import insert


async def processImage(idTest,idPlant,imageB64):
    app_log.info("Processing image with idTest %s and idPlant %s...",idTest,idPlant)
    img_decoded = base64Decode(imageB64)
    imageName = idTest+"-"+idPlant
    saveImage(imageName,img_decoded)
    analyze_results = analyze(os.path.realpath(imageName + ".jpg"))
    insert(idTest,idPlant,analyze_results)
    app_log.info("Image %s succesfully processed ",imageName)

