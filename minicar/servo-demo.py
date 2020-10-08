from __future__ import division
import time
import sys,tty,termios
from servo import CarServo
from servo import _Getch

if __name__ == "__main__":
    pan = 90
    servo = CarServo()
    servo.set_angle(6, 0)
    time.sleep(2)
    servo.set_angle(6, 180)
    time.sleep(2)
    servo.set_angle(6, pan)
    #inkey = _Getch()

    #print("enter ext for quit")
    #try:
    #    while True:
    #        k = inkey(3)
    #        if k == '\x1b[C':
    #            print("right")
    #            pan += 1
    #            servo.set_angle(6, pan)

    #        elif k == '\x1b[D':
    #            print("left")
    #            pan -= 1
    #            servo.set_angle(6, pan)

    #        elif k == 'ext':
    #            print("exit")
    #            servo.set_angle(6, 90)
    #            break
    #        else:
    #            print("not an arrow key!")

    #except KeyboardInterrupt:
    #    pass
