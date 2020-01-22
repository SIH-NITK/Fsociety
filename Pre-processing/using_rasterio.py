import rasterio
from rasterio import plot
import matplotlib as plt
import numpy as np
import os
band_ir=rasterio.open('../awifs_ndvi_201701_15_1_clipped.tif')
band_r=rasterio.open('../awifs_ndvi_201701_15_2_clipped.tif')
red=band_ir.read(1).astype('float64')
ir=band_r.read(1).astype('float64')
ndvi=np.where(
    (ir+red)==0.,
    0,
    (ir-red)/(ir+red)
)
 # print('Ndvi:',ndvi)
ndviImage=rasterio.open('ndviImage.tiff','w',driver='Gtiff',width=band_ir.width, height=band_ir.height, count=1, crs=band_ir.crs, transform=band_ir.transform, dtype='float64')
ndviImage.write(ndvi,1)
ndviImage.close()

ndvi_1=rasterio.open('ndviImage.tiff')
plot.show(ndvi_1)
