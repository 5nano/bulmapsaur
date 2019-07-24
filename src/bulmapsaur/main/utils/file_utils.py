def saveImage(name,img):
    filename = name+'.jpg'  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(img)