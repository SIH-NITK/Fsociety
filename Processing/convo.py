import cv2
import numpy as np
import glob
import scipy.signal as sig
import skimage.measure


files = glob.glob("C:/Users/Skanda/Documents/Machine learning/AgricultureMultispectral/Clipped_NDVI/process2/*.jpg")
#print(files)
convolved = []
i = 0

for file in files:

    img = cv2.imread(file)
        
    img = img[:,:,1]
    
    m,n = img.shape

    test = np.zeros((m,n),dtype=float)
    
    #print(np.logical_and(img[:,:]>160, img[:,:]<220).shape)
    test[np.logical_and(img[:,:]>160, img[:,:]<220)] = img[np.logical_and(img[:,:]>160, img[:,:]<220)]
    
    kernel = np.array([[1,1,1],[1,1,1],[1,1,1]]) *1/9
    
    # convolution 1
    conv1 = sig.convolve2d(test, kernel, 'valid')
    
    # maxpooling 1
    maxpool1 = skimage.measure.block_reduce(conv1, (2,2), np.max)
        
    # convolution 2
    conv2 = sig.convolve2d(maxpool1, kernel, 'valid')
    
    # maxpooling 2
    maxpool2 = skimage.measure.block_reduce(conv2, (2,2), np.max)
    
    
    
    
    # plotting convolved image 
    #cv2.imshow('conv',maxpool2)
    #cv2.waitKey()
    
    cv2.imwrite('./process3/img' + str(i) + '.jpg',maxpool2*255)
    
    convolved.append(maxpool2)
    
    i += 1    


avg_pxl = []
m,n = img.shape

for img in convolved: 
    avg_pxl.append(img.sum()/(m*n))
    

import matplotlib.pyplot as plt

plt.title('average crop pxl value VS month')
plt.plot(range(12),avg_pxl[:12],'r',range(12,24),avg_pxl[12:],'b')
plt.legend(['First year','Second year'])
plt.xlabel('Months')
plt.ylabel('average Crop pxls values')