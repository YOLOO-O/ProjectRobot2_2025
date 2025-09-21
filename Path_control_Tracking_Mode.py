from microbit import *
import machine

MOTOR_LEFT1 = pin0
MOTOR_LEFT2 = pin1
MOTOR_RIGHT1 = pin2
MOTOR_RIGHT2 = pin3

TRACK_LEFT = pin4
TRACK_MID = pin5
TRACK_RIGHT = pin6

for pin in [MOTOR_LEFT1, MOTOR_LEFT2, MOTOR_RIGHT1, MOTOR_RIGHT2]:
    pin.set_pull(pin.PULL_UP)
    pin.write_digital(0)
for track_pin in [TRACK_LEFT, TRACK_MID, TRACK_RIGHT]:
    track_pin.set_pull(track_pin.PULL_DOWN) 

def forward(speed=1):
    MOTOR_LEFT1.write_digital(1)
    MOTOR_LEFT2.write_digital(0)
    MOTOR_RIGHT1.write_digital(1)
    MOTOR_RIGHT2.write_digital(0)
    sleep(int(100/speed)) 

def turn_left(speed=1):
    MOTOR_LEFT1.write_digital(0)
    MOTOR_LEFT2.write_digital(0)
    MOTOR_RIGHT1.write_digital(1)
    MOTOR_RIGHT2.write_digital(0)
    sleep(int(100/speed))

def turn_right(speed=1):
    MOTOR_LEFT1.write_digital(1)
    MOTOR_LEFT2.write_digital(0)
    MOTOR_RIGHT1.write_digital(0)
    MOTOR_RIGHT2.write_digital(0)
    sleep(int(100/speed))

def stop():
    for pin in [MOTOR_LEFT1, MOTOR_LEFT2, MOTOR_RIGHT1, MOTOR_RIGHT2]:
        pin.write_digital(0)

while True:
    left_val = TRACK_LEFT.read_digital()
    mid_val = TRACK_MID.read_digital()
    right_val = TRACK_RIGHT.read_digital()
    
    if mid_val == 1 and left_val == 0 and right_val == 0:
        forward()
    elif left_val == 1 and mid_val == 0 and right_val == 0:
        turn_left()
    elif right_val == 1 and mid_val == 0 and left_val == 0:
        turn_left()
    else:
        stop()