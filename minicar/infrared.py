import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class CarInfrared(object):
    def __init__(self):
        self.infrared_right = 8
        self.infrared_left = 7

        GPIO.setup(self.infrared_right, GPIO.IN)
        GPIO.setup(self.infrared_left, GPIO.IN)

    def infrared(self):
        left = GPIO.input(self.infrared_left)
        right = GPIO.input(self.infrared_right)

        return [left, right]

if __name__ == '__main__':
    try:
        car = CarInfrared()
        while True:
            [left, right] = car.infrared()
            print(left, right)
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
