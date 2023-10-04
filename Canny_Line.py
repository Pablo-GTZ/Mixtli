import cv2
import numpy as np

# Load the input image
image = cv2.imread('linea_izq.jfif')

# Apply Canny edge detection to the image
edges = cv2.Canny(image, threshold1=100, threshold2=200)

# Apply the Hough Transform to detect lines
lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)

# Create a copy of the original image to draw lines on
image_with_lines = image.copy()

# Draw the detected lines on the image
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(image_with_lines, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Draw red lines

# Display the original image, Canny edges, and lines in separate windows
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edges', edges)
cv2.imshow('Image with Detected Lines', image_with_lines)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
