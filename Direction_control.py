from microbit import *
import machine

MOTOR_LEFT1 = pin0
MOTOR_LEFT2 = pin1
MOTOR_RIGHT1 = pin2
MOTOR_RIGHT2 = pin3

for pin in [MOTOR_LEFT1, MOTOR_LEFT2, MOTOR_RIGHT1, MOTOR_RIGHT2]:
    pin.set_pull(pin.PULL_UP)
    pin.write_digital(0)

def forward():
    MOTOR_LEFT1.write_digital(1)
    MOTOR_LEFT2.write_digital(0)
    MOTOR_RIGHT1.write_digital(1)
    MOTOR_RIGHT2.write_digital(0)

def backward():
    MOTOR_LEFT1.write_digital(0)
    MOTOR_LEFT2.write_digital(1)
    MOTOR_RIGHT1.write_digital(0)
    MOTOR_RIGHT2.write_digital(1)

def turn_left():
    MOTOR_LEFT1.write_digital(0)
    MOTOR_LEFT2.write_digital(0)
    MOTOR_RIGHT1.write_digital(1)
    MOTOR_RIGHT2.write_digital(0)

def turn_right():
    MOTOR_LEFT1.write_digital(1)
    MOTOR_LEFT2.write_digital(0)
    MOTOR_RIGHT1.write_digital(0)
    MOTOR_RIGHT2.write_digital(0)

def stop():
    for pin in [MOTOR_LEFT1, MOTOR_LEFT2, MOTOR_RIGHT1, MOTOR_RIGHT2]:
        pin.write_digital(0)

direction_sequence = [forward, backward, turn_left, turn_right, stop]
while True:
    for direction in direction_sequence:
        direction()
        sleep(1000)