import cv2
import numpy as np

# Load the input image
image = cv2.imread('linea_izq.jfif')

# Define the coordinates of the region of interest (ROI)
# Format: (x1, y1) = top-left corner, (x2, y2) = bottom-right corner
height, width, _ = image.shape
roi_x1 = 0  # Left edge of the image
roi_x2 = width*3 // 8  # 1/4 of the image width
roi_y1 = height * 5//8 # Top edge of the image
roi_y2 = height # Full height of the image

# Extract the ROI from the input image
roi = image[roi_y1:roi_y2, roi_x1:roi_x2]

# Apply Canny edge detection to the ROI
edges = cv2.Canny(roi, threshold1=100, threshold2=200)

# Apply the Hough Transform to detect lines in the ROI
lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)

# Create a copy of the original ROI to draw lines on
roi_with_lines = roi.copy()

# Draw the detected lines on the ROI
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
        cv2.line(roi_with_lines, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Draw red lines

# Overlay the ROI with detected lines onto the original image
image_with_lines = image.copy()
image_with_lines[roi_y1:roi_y2, roi_x1:roi_x2] = roi_with_lines

# Display the original image with detected lines
cv2.imshow('Image with Detected Lines', image_with_lines)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
