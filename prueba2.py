from djitellopy import Tello
import cv2

tello=Tello()
tello.connect()

print(tello.get_battery())

tello.set_video_resolution(resolution="480")
tello.set_video_bitrate(bitrate="2 Mbps")

while True:
    
    tello.streamon()

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

cv2.destroyAllWindows()

