import cv2
import numpy as np
from matplotlib import pyplot as pyplot


#Esto cambia por la vista del drone
img =cv2.imread("Pista.jfif", cv2.IMREAD_GRAYSCALE)

canny = cv2.Canny(img, 100, 200)

pyplot.subplot(121)
pyplot.imshow(img, cmap='gray')
pyplot.title('Normal')

pyplot.subplot(122)
pyplot.imshow(canny, cmap='gray')
pyplot.title('Canny')

pyplot.tight_layout()

pyplot.show()