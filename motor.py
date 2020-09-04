import RPi.GPIO as GPIO          
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class CarMotor(object):
    in1 = 23
    in2 = 24
    in3 = 17
    in4 = 27

    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)

    # PWM initialization
    self.motor11 = GPIO.PWM(in1,500)
    self.motor12 = GPIO.PWM(in2,500)
    self.motor21 = GPIO.PWM(in3,500)
    self.motor22 = GPIO.PWM(in4,500)

    self.motor11.start(0)
    self.motor12.start(0)
    self.motor21.start(0)
    self.motor22.start(0)

    def forward(self, speed):
        self.motor11.ChangeDutyCycle(speed)
        self.motor12.ChangeDutyCycle(0)
        self.motor21.ChangeDutyCycle(speed)
        self.motor22.ChangeDutyCycle(0)

    def backward(self, speed):
        self.motor11.ChangeDutyCycle(0)
        self.motor12.ChangeDutyCycle(speed)
        self.motor21.ChangeDutyCycle(0)
        self.motor22.ChangeDutyCycle(speed)

    def left(self, speed):
        self.motor11.ChangeDutyCycle(0)
        self.motor12.ChangeDutyCycle(speed)
        self.motor21.ChangeDutyCycle(speed)
        self.motor22.ChangeDutyCycle(0)

    def right(self, speed):
        self.motor11.ChangeDutyCycle(speed)
        self.motor12.ChangeDutyCycle(0)
        self.motor21.ChangeDutyCycle(0)
        self.motor22.ChangeDutyCycle(speed)

    def forward_turn(self, speed_left, speed_right):
        self.motor11.ChangeDutyCycle(speed_left)
        self.motor12.ChangeDutyCycle(0)
        self.motor21.ChangeDutyCycle(speed_right)
        self.motor22.ChangeDutyCycle(0)

    def brake(self):
        self.motor11.ChangeDutyCycle(0)
        self.motor12.ChangeDutyCycle(0)
        self.motor21.ChangeDutyCycle(0)
        self.motor22.ChangeDutyCycle(0)

    def stop(self):
        self.motor11.stop()
        self.motor12.stop()
        self.motor21.stop()
        self.motor22.stop()

if __name == '__main__':

    try:
        motor = CarMotor()
        print("\n")
        print("The default speed & direction of motor is LOW & Forward.....")
        print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
        print("\n")    

        while(1):
        
            x=raw_input()
            
            if x=='f':
                print("forward")
                motor.forward(26)
                x='z'
        
            elif x=='s':
                print("stop")
                motor.stop()
                x='z'
        
            elif x=='b':
                print("backward")
                motor.backward(26)
                x='z'
        
            elif x=='l':
                print("left")
                motor.left(26)
                x='z'
        
            elif x=='r':
                print("right")
                motor.right(26)
                x='z'
        
            elif x=='e':
                GPIO.cleanup()
                break
            
            else:
                print("<<<  wrong data  >>>")
                print("please enter the defined data to continue.....")
