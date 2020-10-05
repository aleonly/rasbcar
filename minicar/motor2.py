import RPi.GPIO as GPIO          
from time import sleep

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

        self.pa = GPIO.PWM(self.ena, 500)
        self.pa.start(40)
        self.pb = GPIO.PWM(self.enb, 500)
        self.pb.start(40)

    def forward(self):
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.LOW)

    def backward(self):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)

    def left(self):
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)

    def right(self):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.LOW)

    #def forward_turn(self, speed_left, speed_right):
    #    self.motor11.ChangeDutyCycle(speed_left)
    #    self.motor12.ChangeDutyCycle(0)
    #    self.motor21.ChangeDutyCycle(speed_right)
    #    self.motor22.ChangeDutyCycle(0)

    #def brake(self):
    #    self.motor11.ChangeDutyCycle(0)
    #    self.motor12.ChangeDutyCycle(0)
    #    self.motor21.ChangeDutyCycle(0)
    #    self.motor22.ChangeDutyCycle(0)

    def stop(self):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.LOW)

if __name__ == '__main__':
    motor = CarMotor2()
    print("\n")
    print("The default speed & direction of motor is LOW & Forward.....")
    print("s-stop f-forward b-backward left-left r-right l-low m-medium h-high e-exit")
    print("\n")    

    while(1):
        x = input()
        
        if x=='f':
            print("forward")
            motor.forward()
            x='z'
    
        elif x=='s':
            print("stop")
            motor.stop()
            x='z'
    
        elif x=='b':
            print("backward")
            motor.backward()
            x='z'

        elif x=='left':
            print("left")
            motor.left()
            x='z'

        elif x=='r':
            print("right")
            motor.right()
            x='z'
    
        elif x=='l':
            print("low")
            motor.pa.ChangeDutyCycle(30)
            motor.pb.ChangeDutyCycle(30)
            x='z'
    
        elif x=='m':
            print("medium")
            motor.pa.ChangeDutyCycle(50)
            motor.pb.ChangeDutyCycle(50)
            x='z'
    
        elif x=='h':
            print("high")
            motor.pa.ChangeDutyCycle(75)
            motor.pb.ChangeDutyCycle(75)
            x='z'
        
        elif x=='e':
            GPIO.cleanup()
            break
        
        else:
            print("<<<  wrong data  >>>")
            print("please enter the defined data to continue.....")
