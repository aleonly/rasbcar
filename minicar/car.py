import RPi.GPIO as GPIO
import time

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


if __name__ == '__main__':
    try:
        car = Car() 
        #start_time = None

        #while True:
        #    dist_mov_ave = car.moving_distance()
        #    print('Distance', dist_mov_ave)

        #    [left_measure, right_measure] = car.infrared()

        #    if (start_time is None) or (time.time() - start_time >  0.5):
        #        start_time = None
        #        if left_measure == 0 and right_measure == 1:
        #            print("Going right")
        #            car.right()
        #        elif left_measure == 1 and right_measure == 0:
        #            print("Going left")
        #            car.left()
        #        elif left_measure == 0 and right_measure == 0:
        #            print("Going back")
        #            car.backward()
        #        else:
        #            if dist_mov_ave < 20:
        #                car.left()
        #                print("Going left")
        #                start_time = time.time()
        #            elif dist_mov_ave < 100:
        #                car.forward()
        #            else:
        #                car.forward()
        #    else:
        #        pass
        while(1):
            distance = car.distance()
            #print(distance)
            [left_measure, right_measure] = car.infrared()

            #if distance < 30:
            #    car.pa.ChangeDutyCycle(0)
            #    car.pb.ChangeDutyCycle(0)
            #    car.cycle(0)
            #    time.sleep(2)
            #    right_distance = car.distance()
            #    car.cycle(180)
            #    time.sleep(2)
            #    left_distance = car.distance()
            #    car.cycle(90)
            #    time.sleep(2)
            #    
            #    if right_distance < left_distance:
            #        print(right_distance)
            #        car.pa.ChangeDutyCycle(40)
            #        car.pb.ChangeDutyCycle(40)
            #        car.right()
            #        time.sleep(2)
            #    else:
            #        car.pa.ChangeDutyCycle(40)
            #        car.pb.ChangeDutyCycle(40)
            #        car.left()
            #        time.sleep(2)

            #else:
            #    car.pa.ChangeDutyCycle(40)
            #    car.pb.ChangeDutyCycle(40)
            #    if left_measure == 0 and right_measure == 1:
            #        print("Going right")
            #        car.right()
            #    elif left_measure == 1 and right_measure == 0:
            #        print("Going left")
            #        car.left()
            #    else:
            #        car.forward()

      
            car.pa.ChangeDutyCycle(30)
            car.pb.ChangeDutyCycle(30)
            if left_measure == 0 and right_measure == 1:
                print("Going right")
                car.right()
            elif left_measure == 1 and right_measure == 0:
                print("Going left")
                car.left()
            else:
                car.forward()

    except KeyboardInterrupt:
        print("Measurement stopped by User")
        car.all_stop()
