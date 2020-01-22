import cv2
import os
import glob
files = glob.glob("/home/pranav/Downloads/SIH/Clipped_NDVI/*.tif")
j=0
for i in files:
    img = cv2.imread(i)
    crop_img = img[:,0:1700]
    # cv2.imshow("cropped", crop_img)
    cv2.imwrite('./crop/image_crop'+str(j)+'.tif',crop_img)
    j=j+1
    # cv2.waitKey(0)
