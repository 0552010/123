from skimage import io,color
import skimage.morphology as sm
import matplotlib.pyplot as plt
import datetime

starttime = datetime.datetime.now()

img=color.rgb2gray(io.imread('pig_threshold.jpg'))
for i in range (99) :
    dst=sm.closing(img,sm.square(5))  

plt.figure('morphology',figsize=(8,8))
plt.subplot(121)
plt.imshow(img,plt.cm.gray)
plt.axis('off')

plt.subplot(122)
plt.imshow(dst,plt.cm.gray)
plt.axis('off')

endtime = datetime.datetime.now()
print (endtime - starttime)