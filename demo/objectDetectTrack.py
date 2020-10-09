'''
Object detection and tracking with OpenCV
    ==> Turning a LED on detection and
    ==> Real Time tracking with Pan-Tilt servos 

    Based on original tracking object code developed by Adrian Rosebrock
    Visit original post: https://www.pyimagesearch.com/2016/05/09/opencv-rpi-gpio-and-gpio-zero-on-the-raspberry-pi/

Developed by Marcelo Rovai - MJRoBot.org @ 9Feb2018 
'''

# import the necessary packages
from __future__ import print_function
from imutils.video.pivideostream import PiVideoStream
import Adafruit_PCA9685
import argparse
import imutils
import time
import cv2
import os
import RPi.GPIO as GPIO

#define Servos
panServo = 4
tiltServo = 5

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

#position servos 
def positionServo(channel, angle):
    pulse = int(4096*((angle*11)+500)/20000)
    pwm.set_pwm(channel, 0, pulse)
    print("[INFO] Positioning servo at channel {0} to {1} degrees\n".format(channel, angle))

# position servos to present object at center of the frame
def mapServoPosition(x, y):
    global panAngle
    global tiltAngle
    if (x < 270):
        panAngle += 5
        print(panAngle)
        if panAngle > 160:
            panAngle = 160
        positionServo(panServo, panAngle)
 
    if (x > 310):
        panAngle -= 5
        print(panAngle)
        if panAngle < 20:
            panAngle = 20
        positionServo(panServo, panAngle)

    if (y < 190):
        tiltAngle -= 5
        print(tiltAngle)
        if tiltAngle > 160:
            tiltAngle = 160
        positionServo(tiltServo, tiltAngle)
 
    if (y > 240):
        tiltAngle += 5
        print(tiltAngle)
        if tiltAngle < 20:
            tiltAngle = 20
        positionServo(tiltServo, tiltAngle)

# initialize the video stream and allow the camera sensor to warmup
print("[INFO] waiting for camera to warmup...")
vs = PiVideoStream(resolution=(320, 240), framerate=32).start()
time.sleep(2.0)

# define the lower and upper boundaries of the object
# to be tracked in the HSV color space
colorLower = (27, 100, 100)
colorUpper = (47, 255, 255)

# Initialize angle servos at 90-90 position
global panAngle
panAngle = 90
global tiltAngle
tiltAngle =90

# positioning Pan/Tilt servos at initial position
positionServo(panServo, panAngle)
positionServo(tiltServo, tiltAngle)

# loop over the frames from the video stream
while True:
    # grab the next frame from the video stream, Invert 180o, resize the
    # frame, and convert it to the HSV color space
    frame = vs.read()
    frame = imutils.resize(frame, width=600)
    frame = cv2.flip(frame, -1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # construct a mask for the object color, then perform
    # a series of dilations and erosions to remove any small
    # blobs left in the mask
    mask = cv2.inRange(hsv, colorLower, colorUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    
    # find contours in the mask and initialize the current
    # (x, y) center of the object
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)[-2]
    #cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    center = None
    
    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    
        # only proceed if the radius meets a minimum size
        if radius > 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius),
                (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
    
            # position Servo at center of circle
            mapServoPosition(int(x), int(y))
    		
    # if the ball is not detected
    else:
        print("ball not detected")
        
    # show the frame to our screen
    cv2.imshow("Frame", frame)
    
    # if [ESC] key is pressed, stop the loop
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

# do a bit of cleanup
print("\n[INFO] Exiting Program and cleanup stuff \n")
positionServo(panServo, 90)
positionServo(tiltServo, 90)
cv2.destroyAllWindows()
vs.stop()
