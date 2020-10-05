import RPi.GPIO as GPIO
import time
  
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
  
GPIO_TRIGGER = 5
GPIO_ECHO = 6

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    GPIO.output(GPIO_TRIGGER, False) 
    time.sleep(0.000002)
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    ii = 0
    while GPIO.input(GPIO_ECHO) == 0:
        ii = ii + 1
        if ii > 10000: 
            print('Ultrasound error: the sensor missed the echo')
            return 0
        pass

    start_time = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        pass

    stop_time = time.time()

    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2

    return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print("Measured Distance = {:.2f} cm".format(dist))
            time.sleep(1)
  
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
