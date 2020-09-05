import RPi.GPIO as GPIO
import time

from motor2 import CarMotor2
from ultrasonic import CarUltrasonic
from infrared import CarInfrared

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class Car(CarMotor2,CarUltrasonic, CarInfrared):
    def __init__(self):
        CarMotor2.__init__(self)
        CarUltrasonic.__init__(self)
        CarInfrared.__init__(self)
    
    def all_stop(self):
        CarMotor2.stop(self)
        GPIO.cleanup()


if __name__ == '__main__':
    try:
        car = Car() 
        start_time = None

        while True:
            dist_mov_ave = car.moving_distance()
            print('Distance', dist_mov_ave)

            [left_measure, right_measure] = car.infrared()

            if (start_time is None) or (time.time() - start_time >  0.5):
                start_time = None
                if left_measure == 0 and right_measure == 1:
                    print("Going right")
                    car.right()
                elif left_measure == 1 and right_measure == 0:
                    print("Going left")
                    car.left()
                elif left_measure == 0 and right_measure == 0:
                    print("Going back")
                    car.backward()
                else:
                    if dist_mov_ave < 20:
                        car.left()
                        print("Going left")
                        start_time = time.time()
                    elif dist_mov_ave < 100:
                        car.forward()
                    else:
                        car.forward()
            else:
                pass

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        car.all_stop()
