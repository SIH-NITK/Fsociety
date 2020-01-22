import cv2
import numpy as np
import glob
import scipy.signal as sig
import skimage.measure


files = glob.glob("/home/pranav/Downloads/SIH/Clipped_NDVI/testing/combined_bands/*.jpg")
#print(files)
convolved = []
v=0
for file in files:

    img = cv2.imread(file)

    m,n,_ = img.shape

    test = np.zeros((m,n),dtype=float)

    test[np.logical_and(img[:,:,1]>160, img[:,:,1]<220)] = np.copy(img[np.logical_and(img[:,:,1]>160, img[:,:,1]<220)])

    kernel = np.array([[1,1,1],[1,1,1],[1,1,1]]) *1/9

    # convolution 1
    conv1 = sig.convolve2d(test, kernel, 'valid')

    # maxpooling 1
    maxpool1 = skimage.measure.block_reduce(conv1, (2,2), np.max)

    # convolution 2
    conv2 = sig.convolve2d(maxpool1, kernel, 'valid')

    # maxpooling 2
    maxpool2 = skimage.measure.block_reduce(conv2, (2,2), np.max)


    #
    cv2.imwrite('./processed_cnn/image'+str(v)+'.jpg')
    # cv2.imshow('conv',maxpool2)
    # cv2.waitKey()
    v+=1
    convolved.append(maxpool2)
