from __future__ import division
import time
import Adafruit_PCA9685
import sys,tty,termios

class CarServo(object):
    def __init__(self):
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.pwm.set_pwm_freq(50)

    def set_angle(self, channel, angle):
        pulse = int(4096*((angle*11)+500)/20000)
        self.pwm.set_pwm(channel, 0, pulse)

class _Getch:
    def __call__(self, n):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(n)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

if __name__ == "__main__":
    pan = 90
    tilt = 90
    servo = CarServo()
    servo.set_angle(4, pan)
    servo.set_angle(5, tilt)
    inkey = _Getch()

    print("enter ext for quit")
    try:
        while True:
            k = inkey(3)
            if k == '\x1b[A':
                print("up")
                tilt -= 1
                servo.set_angle(5, tilt)

            elif k == '\x1b[B':
                print("down")
                tilt += 1
                servo.set_angle(5, tilt)

            elif k == '\x1b[C':
                print("right")
                pan += 1
                servo.set_angle(4, pan)

            elif k == '\x1b[D':
                print("left")
                pan -= 1
                servo.set_angle(4, pan)

            elif k == 'ext':
                print("exit")
                servo.set_angle(4, 90)
                servo.set_angle(5, 90)
                break
            else:
                print("not an arrow key!")

    except KeyboardInterrupt:
        pass
