import cv2
import numpy as np
import glob

files = glob.glob("C:/Users/Skanda/Documents/Machine learning/AgricultureMultispectral/Clipped_NDVI/process2/*.jpg")
#print(files)

count_tot=[]
second_count=[]

for file in files:

    img = cv2.imread(file)

    m,n,_ = img.shape

    test = np.copy(img[:,:,1])
    
    # print('Test is:',test)
    
    count_tot.append(np.count_nonzero(test > 127))
    
    second_count.append(np.count_nonzero(np.logical_and(test>160,test<220)))
    




print('Total summation for each image')
print(count_tot)
print('Selected summation')
print(second_count)


# Visualizing data
import matplotlib.pyplot as plt

plt.title('No. crop pxl VS month')
plt.plot(range(12),second_count[:12],'ro',range(12),second_count[12:],'bo')
plt.legend(['First year','Second year'])
plt.xlabel('Months')
plt.ylabel('No. of Crop pxls')


ratios = [i/j for i,j in zip(second_count,count_tot)]

plt.title('ratio of crop pxl VS month')
plt.plot(range(12),ratios[:12],'ro',range(12),ratios[12:],'bo')
plt.legend(['First year','Second year'])
plt.xlabel('Months')
plt.ylabel('ratios of Crop pxls')




