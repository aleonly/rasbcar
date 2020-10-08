from __future__ import division
import RPi.GPIO as GPIO          
from time import sleep
import sys,tty,termios

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class CarMotor2(object):
    def __init__(self):
        self.in1 = 23
        self.in2 = 24
        self.ena = 25
        self.in3 = 17
        self.in4 = 27
        self.enb = 22

        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.ena, GPIO.OUT)

        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.setup(self.in4, GPIO.OUT)
        GPIO.setup(self.enb, GPIO.OUT)

        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)

        self.pa = GPIO.PWM(self.ena, 1000)
        self.pa.start(40)
        self.pb = GPIO.PWM(self.enb, 1000)
        self.pb.start(40)

    def forward(self, speed=40):
        self.pa.ChangeDutyCycle(speed)
        self.pb.ChangeDutyCycle(speed)
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.LOW)

    def backward(self, speed=40):
        self.pa.ChangeDutyCycle(speed)
        self.pb.ChangeDutyCycle(speed)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)

    def left(self, speed=40):
        self.pa.ChangeDutyCycle(speed)
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)

    def right(self, speed=40):
        self.pb.ChangeDutyCycle(speed)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.LOW)

    def forward_turn(self, speed_left, speed_right):
        self.pa.ChangeDutyCycle(speed_left)
        self.pb.ChangeDutyCycle(speed_right)
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)

    def brake(self):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.LOW)

    def stop(self):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.LOW)

    def speed(self, cycle):
        ena.ChangeDutyCycle(cycle)
        enb.ChangeDutyCycle(cycle)

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
    motor = CarMotor2()
    inkey = _Getch()
    print("\n")
    print("The default speed & direction of motor is LOW & Forward.....")
    print("s-stop f-forward b-backward left-left r-right l-low m-medium h-high e-exit")
    print("\n")

    print("enter q for quit")
    try:
        while True:
            k = inkey(1)
            if k == 'w':
                print("forward")
                motor.forward()

            elif k == 'x':
                print("backward")
                motor.backward()

            elif k == 'a':
                print("left")
                motor.left(70)

            elif k == 'd':
                print("right")
                motor.right(70)

            elif k == 's':
                print("stop")
                motor.stop()

            elif k == 'q':
                GPIO.cleanup()
                break
            else:
                print("<<<  wrong data  >>>")
                print("please enter the defined data to continue.....")

    except KeyboardInterrupt:
        pass
