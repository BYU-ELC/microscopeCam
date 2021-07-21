
import cv2
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
clock = Timer()

button = Button(14)

end = 600 # time in seconds to run

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
textColor = (255, 0, 255)
  
# Line thickness of 2 px
thickness = 2

while True:
    print(clock.get())
    timeLeft = end - round(clock.get());

    ret, frame = vs.read()
    # frame = cv2.flip(frame, 1)

    if (timeLeft <= 30):
        cv2.putText(frame, str(timeLeft), org, font, fontScale, textColor, thickness, cv2.LINE_AA)

    cv2.imshow("camera", frame)

    k = cv2.waitKey(1)
    if k == ord('r') or (button.is_pressed):
        clock.reset();
    if k == ord('q'):
        break
    if timeLeft <= 0:
        break

