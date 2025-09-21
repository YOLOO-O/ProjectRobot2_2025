from microbit import *
import machine

MOTOR_LEFT1 = pin0
MOTOR_LEFT2 = pin1
MOTOR_RIGHT1 = pin2
MOTOR_RIGHT2 = pin3

pins = [MOTOR_LEFT1, MOTOR_LEFT2, MOTOR_RIGHT1, MOTOR_RIGHT2]
for pin in pins:
    pin.set_pull(pin.PULL_UP)
    pin.write_digital(0)

def motor_forward():
    MOTOR_LEFT1.write_digital(1)
    MOTOR_LEFT2.write_digital(0)
    MOTOR_RIGHT1.write_digital(1)
    MOTOR_RIGHT2.write_digital(0)

def motor_stop():
    for pin in [MOTOR_LEFT1, MOTOR_LEFT2, MOTOR_RIGHT1, MOTOR_RIGHT2]:
        pin.write_digital(0)

while True:
    motor_forward()
    sleep(3000)  
    motor_stop()
    sleep(1000) 