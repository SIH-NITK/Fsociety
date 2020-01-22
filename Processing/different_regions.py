
import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt

files = glob.glob("C:/Users/Skanda/Documents/Machine learning/AgricultureMultispectral/Clipped_NDVI/process2/*.jpg")
#print(files)

images = []

for file in files:
    
    img = cv2.imread(file)
    
    img = img[:,:,1]
    
    images.append(img)
    
    
m,n = images[0].shape
p = 500


for i in range(0,m,p//2):
    for j in range(0,n,p//2):
        
        avg_pxl = []
        for img in images:
            avg_pxl.append(img[i:i+p,j:j+p].sum() / (p**2))
            
        plt.plot(range(24),avg_pxl)
        plt.title('Region_'+str(i)+'_'+str(j))
        plt.xlabel('Months')
        plt.ylabel('Avg pxl values')
        
        plt.savefig('Region_'+str(i)+'_'+str(j)+'.png')
        
        #input()