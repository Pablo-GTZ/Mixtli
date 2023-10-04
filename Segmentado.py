import cv2

# Load the image
image = cv2.imread('Rline.jpeg')

height,width,_ = image.shape

# Define the number of columns you want to split the image into
num_columns = 4  # Change this to the desired number of columns

# Calculate the width of each column
column_width = width // num_columns

# Initialize a list to store the columns
columns = []

# Split the image into columns using a for loop
for i in range(num_columns):
    start_col = i * column_width
    end_col = (i + 1) * column_width

    # Extract the current column
    column = image[:, start_col:end_col]
    columns.append(column)

# Display or save the columns as needed
for i, column in enumerate(columns):
    cv2.imshow(f'Column {i+1}', column)

cv2.waitKey(0)
cv2.destroyAllWindows()