import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class CarServo(object):
    def __init__(self):
        self.pin = 16
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.LOW)
        self.p=GPIO.PWM(self.pin, 50)
        self.p.start(0)

    def cycle(self, r):
        self.p.ChangeDutyCycle(2+r/18)

if __name__ == "__main__":
    servo = CarServo()
    info = "please input the degree(0<=a<=180)\nor press q to quit\n"
    r = input(info)

    try:
        while not r == "q":
            if r.isdigit():
                r = int(r)
            else:
                print("please input a number(0<=num<=180)")
                continue

            if r < 0 or r > 180:
                print("a must be [0,180]")
                continue

            servo.cycle(r)
            time.sleep(0.02)

            r=str(input(info))
    except KeyboardInterrupt:
        pass

    servo.p.stop()
    GPIO.cleanup()
