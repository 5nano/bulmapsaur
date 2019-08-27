from datetime import datetime
import time
import os
import re
import image_service as imageService
import utils.encode_utils as encodeUtils
import asyncio

def run():
    while 1:
        t = datetime.now()
        for e in images():
            print("reprocessing "+ e)
            splitedImage = e.split("-")
            base64Image = encodeUtils.base64encode(os.getcwd()+"/bulmapsaur-images/"+e)
            loop = asyncio.get_event_loop()
            loop.run_until_complete(imageService.processImage(splitedImage[0],splitedImage[1], base64Image,e))

        time.sleep(60*2)


def images():
    rootdir = os.getcwd()
    regex = re.compile('(.*jpg$)')
    images = []
    for root, dirs, files in os.walk(rootdir+"/bulmapsaur-images/"):
        for file in files:
            if regex.match(file):
                images.append(file)
    return images