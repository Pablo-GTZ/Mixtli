import cv2
import numpy as np
from matplotlib import pyplot as pyplot


numimagenes = 5

#Esto cambia por la vista del drone
img =cv2.imread("Pista.jfif", cv2.IMREAD_GRAYSCALE)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3) #Ksize = courner size
#Absolute value
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) #El ultimo argumento cambia X y Y
sobelX = np.uint8(np.absolute(sobelX))

sobelY = cv2.Sobel(img,cv2.CV_64F, 0, 1)
sobelY = np.uint8(np.absolute(sobelY))


canny = cv2.Canny(img, 100, 200)

titles =['image', 'Laplacian', 'SobelX','SobelY', 'Canny']
images = [img, lap, sobelX, sobelY, canny]


for i in range (numimagenes):
    pyplot.subplot(1, numimagenes, i+1), pyplot.imshow(images[i], 'gray')
    pyplot.title(titles[i])
    pyplot.xticks([]),pyplot.yticks([])

pyplot.show()
