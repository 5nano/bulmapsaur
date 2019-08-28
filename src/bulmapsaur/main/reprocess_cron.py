import os
import re
import threading
import time
from multiprocessing import Process

import schedule
from tornado.log import app_log

import image_service as imageService
import utils.encode_utils as encodeUtils


def run():
    print("lucas")
    for imageName in images():
        app_log.info("Reprocessing %s", imageName)
        base64Image = encodeUtils.base64encode(
            os.getcwd()+"/bulmapsaur-images/"+imageName)
        threading.Thread(target=imageService.processImage,
                         args=(imageName, base64Image, False))


def images():
    rootdir = os.getcwd()
    regex = re.compile('(.*jpg$)')
    images = []
    for root, dirs, files in os.walk(rootdir+"/bulmapsaur-images/"):
        for file in files:
            if regex.match(file):
                images.append(file)
    app_log.info("%s to reprocess", len(images))
    return images


def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(10)


if __name__ == "__main__":
    schedule.every(2).minutes.do(run)
    try:
        process = Process(target=run_schedule)
        process.start()
        process.join()
    except KeyboardInterrupt:
        process.terminate()
