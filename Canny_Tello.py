#Asies, lo saque de chat y no lo he provado 

import cv2
from djitellopy import Tello

# Create a Tello object and connect to the drone
tello = Tello()
tello.connect()
tello.streamon()

while True:
    # Receive a frame from the Tello drone
    frame = tello.get_frame_read().frame

    # Apply Canny edge detection to the frame
    edges = cv2.Canny(frame, threshold1=100, threshold2=200)  # Adjust thresholds as needed

    # Display the original frame and the processed edges
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Edges", edges)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the video display and end the connection
cv2.destroyAllWindows()
tello.streamoff()
tello.end()
