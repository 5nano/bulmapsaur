import encode_utils as  encodeUtils
import image_analyzer as imageAnalyzer
import file_utils as fileUtils


async def processImage(imageName,imageB64):
    print("Processing image ...")
    img_decoded = encodeUtils.base64Decode(imageB64)
    fileUtils.saveImage(imageName,img_decoded)
    #imageAnalyzer.analyze(imageName+".jpg")
