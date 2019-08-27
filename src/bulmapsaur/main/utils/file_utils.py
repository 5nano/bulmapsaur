import os

def saveImage(name,img):
    if not os.path.exists(os.getcwd()+"/bulmapsaur-images"):
        os.makedirs(os.getcwd()+"/bulmapsaur-images")
    filename = os.path.join(os.getcwd()+"/bulmapsaur-images",name+'.jpg')  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(img)