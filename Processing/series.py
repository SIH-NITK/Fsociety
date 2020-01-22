import cv2
import numpy as np
import glob

files = glob.glob("/home/pranav/Downloads/SIH/Clipped_NDVI/testing/combined_bands/*.jpg")
print(files)
count_tot=[]
second_count=[]
for file in files:
    count=0
    tot=0
    print(file)
    img = cv2.imread(file)
    #
    m,n,_ = img.shape
    print(m,'   ',n)
    img_copy = np.copy(img)
    img_copy[:,:,0] = np.zeros((m,n))
    img_copy[:,:,2] = np.zeros((m,n))
    tm=img_copy[:,:,0]
    test=img_copy[:,:,1]
    # print('Test is:',test)
    for j in range(len(test)):
        for k in range(len(test[j])):
            if test[j][k]>127:
                count=count+test[j][k]
            if test[j][k]>=160 and test[j][k]<=220:
                tot=tot+test[j][k]

    count_tot.append(count)
    second_count.append(tot)

print('Total summation for each image')
print(count_tot)
print('Selected summation')
print(second_count)
