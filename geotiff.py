import numpy as np
import gdal
import cv2

ds = gdal.Open('0p2step_raster.tif', gdal.GA_ReadOnly)
a = np.array([ds.GetRasterBand(i + 1).ReadAsArray() for i in range(ds.RasterCount)])
print(a.shape)
print("x:" + str(ds.RasterXSize), "y:" + str(ds.RasterYSize))

a = a.reshape(ds.RasterYSize, ds.RasterXSize)
print a.shape
dem_img = cv2.Canny(a, 50, 110)

cv2.imshow("dem", dem_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

