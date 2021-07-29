
import cv2
from cv2 import VideoCapture
import time

import RPi.GPIO as GPIO
 
class Timer:
    def __init__(self):
        self.start = time.time()

    def reset(self):
        self.start = time.time()

    def get(self):
        return time.time() - self.start


vs = cv2.VideoCapture(0)
# vs.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
# vs.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)

vs.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
vs.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)




clock = Timer()

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP) # use internal pull up
'''
Oh, the grand old Duke of York
He had ten thousand men
He marched them up to the top of the hill
And he marched them down again
And when they were up, they were up
And when they were down, they were down
And when they were only half-way up
They were neither up nor down
'''

end = 600 # time in seconds to run

font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
textColor = (255, 0, 255)
thickness = 2
window_name = "Microscope"
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

credits = True;

while True:
    # print(clock.get())
    timeLeft = end - round(clock.get())

    ret, frame = vs.read()
    frame = cv2.resize(frame,(1920,1440),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
    # frame = cv2.flip(frame, 1)

    if (timeLeft > (end - 3)) and credits:
        cv2.putText(frame, "Made by Casey", org, font, fontScale, textColor, thickness, cv2.LINE_AA)

    if (timeLeft <= 30):
        cv2.putText(frame, "Shutting down in: " + str(timeLeft), org, font, fontScale, textColor, thickness, cv2.LINE_AA)
        cv2.putText(frame, "Smash the big red button on the right of the table to reset the timer", (50, 80), font, fontScale, textColor, thickness, cv2.LINE_AA)

    cv2.imshow(window_name, frame)

    k = cv2.waitKey(1)
    if (k == ord('r')) or (GPIO.input(14)):
    # if k == ord('r'):
        clock.reset()
        credits = False
    if k == ord('q'):
        break
    if timeLeft <= 0:
        break


# cleanup
vs.release()
cv2.destroyAllWindows()

