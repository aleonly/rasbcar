import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class Servo(object):
    def __init__(self, channel):
        self.channel = channel
        GPIO.setup(self.channel, GPIO.OUT, initial=GPIO.LOW)
        self.pwm=GPIO.PWM(self.channel, 50)
        self.pwm.start(0)

    def duty_cycle(self, angle):
        self.pwm.ChangeDutyCycle(2+angle/18)

if __name__ == "__main__":
    servo = Servo(26)

    try:
        while True:
            angle = input("Please enter a integer [0,180]:")

            if angle == "q":
                break
            
            if not angle.isdigit():
                print("angle must be integer")
                continue

            if int(angle) < 0 or int(angle) > 180:
                print("angle must be [0,180]")
                continue

            servo.duty_cycle(angle)
            time.sleep(0.02)

    except KeyboardInterrupt:
        pass

    servo.pwm.stop()
    GPIO.cleanup()
