from tornado.log import app_log
from utils.encode_utils import base64Decode
from utils.file_utils import saveImage
from datetime import datetime
import os
from plantcv_service import analyze
from cassandra_connector import insert


async def processImage(imageName, imageB64, shouldSave:True):
    img_decoded = base64Decode(imageB64)
    if(shouldSave):
        saveImage(imageName,img_decoded)
    try:
        app_log.info("Processing image %s", imageName)
        analyzed_results = analyze(os.path.realpath("bulmapsaur-images/"+imageName))
        app_log.info("Persisting image %s ...", imageName)
        insert(getIdTest(imageName), getIdPlant(imageName), analyzed_results, imageB64)
    except:
        app_log.info("Image %s was not succesfully processed ", imageName)
    else:
        app_log.info("Deleting Image %s from disk ", imageName)
        path = os.path.join(os.getcwd()+"/bulmapsaur-images/", imageName)
        os.remove(path)
        app_log.info("Image %s succesfully processed ", imageName)

def getIdTest(imageName):
    return  imageName.split("-")[0]

def getIdPlant(imageName):
    return  imageName.split("-")[1]

