
import cv2
from cv2 import VideoCapture
import time

from gpiozero import Button
 
class Timer:
    def __init__(self):
        self.start = time.time()

    def reset(self):
        self.start = time.time()

    def get(self):
        return time.time() - self.start


vs = cv2.VideoCapture(0)
vs.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
vs.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)

clock = Timer()

button = Button(14)

end = 600 # time in seconds to run

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
textColor = (255, 0, 255)
window_name = "Microscope"
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# Line thickness of 2 px
thickness = 2

while True:
    # print(clock.get())
    timeLeft = end - round(clock.get())

    ret, frame = vs.read()
    # frame = cv2.flip(frame, 1)

    if (timeLeft <= 30):
        cv2.putText(frame, "Shutting down in: " + str(timeLeft), org, font, fontScale, textColor, thickness, cv2.LINE_AA)

    cv2.imshow(window_name, frame)

    k = cv2.waitKey(1)
    if k == ord('r') or (button.is_pressed):
    # if k == ord('r'):
        clock.reset()
    if k == ord('q'):
        break
    if timeLeft <= 0:
        break


# cleanup
vs.release()
cv2.destroyAllWindows()

