# Simple code to read a message from the Dabble App over the DSDTech HM-10 bluetooth module
# Author: Eric Z. Ayers <ericzundel@gmail.com>

"""CircuitPython Example of how to read data from the Dabble app"""
import binascii
import board
import busio
import digitalio
import time
import pwmio
from adafruit_motor import servo

# create a PWMOut object on Pin A2.
pwm1 = pwmio.PWMOut(board.GP21, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.GP19, duty_cycle=2 ** 15, frequency=50)
pwm3 = pwmio.PWMOut(board.GP16, duty_cycle=2 ** 15, frequency=50)
pwm4 = pwmio.PWMOut(board.GP17, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
left = servo.Servo(pwm1)
right = servo.Servo(pwm2)
left_arm = servo.Servo(pwm4)
right_arm = servo.Servo(pwm3)

from dabble import Dabble

dabble = Dabble(board.GP0, board.GP1, debug=True)


def forward():
    left.angle = 180
    right.angle = 0

def backward():
    left.angle = 0
    right.angle = 180

def left_turn():
    left.angle = 0
    right.angle = 0

def right_turn():
    left.angle = 180
    right.angle = 180

def left_arm_move():
    left_arm.angle = 180
    time.sleep(.5)
    left_arm.angle = 0
    time.sleep(.5)

def right_arm_move():
    right_arm.angle = 180
    time.sleep(.5)
    right_arm.angle = 0
    time.sleep(.5)


def stop():
    left.angle = 90
    right.angle = 90

while True:
    message = dabble.read_message()
    if (message != None):
        print("Message: " + str(message))
        # Implement tank steering on a 2 wheeled robot
        if (message.up_arrow_pressed):
            forward()
            print("Move both motors forward")
        elif (message.down_arrow_pressed):
            print("Move both motors backward")
            backward()
        elif (message.right_arrow_pressed):
            print("Move left motor forward and right motor backward")
            right_turn()
        elif (message.left_arrow_pressed):
            print("Move left motor backward and right motor forward")
            left_turn()
        elif (message.no_direction_pressed):
            print("Stop both motors")
            stop()
        else:
            print("Something crazy happened with direction!")

        if (message.triangle_pressed):
            print("Raise left arm")
            left_arm_move()
        elif (message.circle_pressed):
            print("Lower right arm")
            right_arm_move()
        elif (message.square_pressed):
            print("Squirt water")
        elif (message.circle_pressed):
            print("Fire laser")
        elif (message.start_pressed):
            print("Turn on LED")
        elif (message.select_pressed):
            print("Do victory dance")
        elif (message.no_action_pressed):
            print("No action")
        else:
            print("Something crazy happened with action!")
