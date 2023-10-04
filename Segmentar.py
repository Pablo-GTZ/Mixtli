import cv2

# Load the image
image = cv2.imread('Rline.jpeg')
cv2.imshow('Rline.jepg')

# Get the dimensions of the image
height, width, _ = image.shape

# Calculate the width of each column
column_width = width // 2

# Split the image into two columns
column1 = image[:, :column_width]
column2 = image[:, column_width:]

# Display the two columns (you can also save them if needed)
cv2.imshow('Column 1', column1)
cv2.imshow('Column 2', column2)
cv2.waitKey(0)
cv2.destroyAllWindows()