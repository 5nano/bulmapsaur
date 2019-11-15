import os
import errno
def saveImage(name,img):
    filename = 'images/'+name+'.jpg'  # I assume you have a way of picking unique filenames
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "wb") as f:
        f.write(img)