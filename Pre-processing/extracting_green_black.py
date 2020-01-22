import cv2
import numpy as np
import glob

files = glob.glob("/home/pranav/Downloads/SIH/Clipped_NDVI/*.tif")

i = 0
for file in files:
    print(file)
    img = cv2.imread(file)
    #
    m,n,_ = img.shape
    print(m,'   ',n)

    #
    img_copy = np.copy(img)
    img_copy[:,:,0] = np.zeros((m,n))
    img_copy[:,:,2] = np.zeros((m,n))
    tm=img_copy[:,:,0]
    test=img_copy[:,:,1]
    print('Test is:',test)
    for j in range(len(test)):
        for k in range(len(test[j])):
            if test[j][k]<125:
                test[j][k]=0
    #

    img_copy[:,:,1]=test
    cv2.imwrite(str(i)+"_processed_convert.tif",img_copy)
    #
    i += 1

cv2.imshow('green channel',img_copy)
