import cv2
import numpy as np
import glob

files = glob.glob("/home/pranav/Downloads/SIH/Clipped_NDVI/awifs_ndvi_201708_15_1_clipped.tif")

k = 0
for file in files:

    img = cv2.imread(file)

    m,n,_ = img.shape

    img_copy = np.copy(img)

    img_copy = img_copy[:,:,0]

    img_copy = img_copy*2/255 - 1

    m,n,_ = img.shape
    for i in range(m):
        for j in range(n):

            if img_copy[i,j] < -0.42 and img_copy[i,j] > -0.85:
                img[i,j,0] = 144
                img[i,j,1] = 238
                img[i,j,2] = 144

            elif img_copy[i,j] < -0.85:
                img[i,j,0] = 29
                img[i,j,1] = 101
                img[i,j,2] = 181

            else:
                img[i,j,0] = 255
                img[i,j,1] = 255
                img[i,j,2] = 255


    #cv2.imwrite("./process2/img"+str(k)+".jpg",img)
    cv2.imshow("proc",img/255)

    cv2.waitKey()

    k += 1


cv2.destroyAllWindows()
