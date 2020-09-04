import RPi.GPIO as GPIO
import time
  
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
  
class CarUltrasonic(object):
    def __init__(self):

        self.GPIO_TRIGGER = 5
        self.GPIO_ECHO = 6

        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)

        self.dist_mov_ave = 0
  
    def distance(self):
        GPIO.output(self.GPIO_TRIGGER, False) 
        time.sleep(0.000002)
        GPIO.output(self.GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)

        ii = 0
        while GPIO.input(self.GPIO_ECHO) == 0:
            ii = ii + 1
            if ii > 10000: 
                print('Ultrasound error: the sensor missed the echo')
                return 0
            pass

        start_time = time.time()

        while GPIO.input(self.GPIO_ECHO) == 1:
            pass

        stop_time = time.time()
    
        time_elapsed = stop_time - start_time
        distance = (time_elapsed * 34300) / 2
    
        return distance

if __name__ == '__main__':
    try:
        car = CarUltrasonic()
        while True:
            dist = car.distance()
            print("Measured Distance = {:.2f} cm".format(dist))
            time.sleep(1)
  
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
