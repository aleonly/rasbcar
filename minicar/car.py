import RPi.GPIO as GPIO
import time
import sys,tty,termios

from motor2 import CarMotor2
from ultrasonic import CarUltrasonic
from infrared import CarInfrared
from servo import CarServo

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class Car(CarMotor2,CarUltrasonic, CarInfrared, CarServo):
    def __init__(self):
        CarMotor2.__init__(self)
        CarUltrasonic.__init__(self)
        CarInfrared.__init__(self)
        CarServo.__init__(self)
    
    def all_stop(self):
        CarMotor2.stop(self)
        GPIO.cleanup()

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

if __name__ == '__main__':
    try:
        car = Car() 
        ultrasonic_pan = 90
        car.set_angle(6, ultrasonic_pan)

        while(1):
            distance = car.distance()
            [left_measure, right_measure] = car.infrared()

            car.pa.ChangeDutyCycle(40)
            car.pb.ChangeDutyCycle(40)

            if distance > 30:
                if left_measure == 0 and right_measure == 1:
                    print("Going right")
                    car.right(70)
                elif left_measure == 1 and right_measure == 0:
                    print("Going left")
                    car.left(70)
                else:
                    car.forward()
            else:
                car.stop()
                car.set_angle(6, 0)
                right_distance = car.distance()
                time.sleep(1)
                car.set_angle(6, 180)
                left_distance = car.distance()
                time.sleep(1)
                car.set_angle(6, 90)

                if right_distance < left_distance:
                    print("Fence, going right")
                    car.right(70)
                    time.sleep(1)
                else:
                    print("Fence, going left")
                    car.left(70)
                    time.sleep(1)

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        car.set_angle(6, ultrasonic_pan)
        car.all_stop()
