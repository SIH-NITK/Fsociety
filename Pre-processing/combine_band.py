import cv2
import numpy as np
import glob

NIR = sorted(glob.glob("/home/pranav/Downloads/SIH/Clipped_NDVI/testing/Ir_band/*.tif"))#.sort()
IR = sorted(glob.glob("/home/pranav/Downloads/SIH/Clipped_NDVI/testing/Red_band/*.tif"))#.sort()
k = 0
for nir,ir in zip(NIR,IR):

    img_nir = cv2.imread(nir)
    img_ir = cv2.imread(ir)

    img_nir = img_nir[:,:,0]
    img_ir = img_ir[:,:,0]

    m,n = img_nir.shape

    ndvi = np.where((img_nir+img_ir) == 0,0,(img_nir-img_ir)/(img_nir+img_ir))

    img = np.zeros((m,n,3),dtype=float)

    for i in range(m):
        for j in range(n):

            if ndvi[i,j] > 0.45:
                img[i,j,0] = 0
                img[i,j,1] = 100
                img[i,j,2] = 0

            elif ndvi[i,j] > 0.1:
                img[i,j,0] = 144
                img[i,j,1] = 238
                img[i,j,2] = 144

            elif ndvi[i,j] > -0.5:
                img[i,j,0] = 0
                img[i,j,1] = 75
                img[i,j,2] = 150

            else:
                img[i,j,0] = 255
                img[i,j,1] = 255
                img[i,j,2] = 255


    cv2.imwrite("./combined_bands/img"+str(k)+".jpg",img)
    # cv2.imshow("proc",img/255)
    #
    # cv2.waitKey()

    k += 1

cv2.destroyAllWindows()
