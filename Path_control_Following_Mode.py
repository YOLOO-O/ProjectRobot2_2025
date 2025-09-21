from microbit import *
import machine

MOTOR_LEFT1 = pin0
MOTOR_LEFT2 = pin1
MOTOR_RIGHT1 = pin2
MOTOR_RIGHT2 = pin3

FOLLOW_LEFT = pin9
FOLLOW_RIGHT = pin10

for pin in [MOTOR_LEFT1, MOTOR_LEFT2, MOTOR_RIGHT1, MOTOR_RIGHT2]:
    pin.set_pull(pin.PULL_UP)
    pin.write_digital(0)
for follow_pin in [FOLLOW_LEFT, FOLLOW_RIGHT]:
    follow_pin.set_pull(follow_pin.PULL_UP) 

def forward():
    MOTOR_LEFT1.write_digital(1)
    MOTOR_LEFT2.write_digital(0)
    MOTOR_RIGHT1.write_digital(1)
    MOTOR_RIGHT2.write_digital(0)

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

while True:
    left_sig = FOLLOW_LEFT.read_digital()
    right_sig = FOLLOW_RIGHT.read_digital()

    if left_sig == 0 and right_sig == 0:
        forward()
    elif left_sig == 0 and right_sig == 1:
        turn_left()
    elif right_sig == 0 and left_sig == 1:
        turn_right()
    else:
        stop()
    sleep(100) 