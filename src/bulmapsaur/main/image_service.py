from tornado.log import app_log
from utils.encode_utils import base64Decode
from utils.file_utils import saveImage
from datetime import datetime
import os

#from image_analyzer import analyze
from plantcv_service import analyze
from cassandra_connector import insert


async def processImage(idTest,idPlant,imageB64):
    app_log.info("Processing image with idTest %s and idPlant %s...",idTest,idPlant)
    img_decoded = base64Decode(imageB64)
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
    imageName = idTest+"-"+idPlant+"-"+dt_string
    saveImage(imageName,img_decoded)
    try:
        analyze_results = analyze(os.path.realpath(imageName + ".jpg"))
        app_log.info("Persisting image %s ...", imageName)
        insert(idTest, idPlant, analyze_results, imageB64)
    except:
        app_log.info("Image %s was not succesfully processed ", imageName)
    else:
        app_log.info("Deleting Image %s from disk ", imageName)
        path = os.path.join(os.getcwd(), imageName+".jpg")
        os.remove(path)
        app_log.info("Image %s succesfully processed ", imageName)

