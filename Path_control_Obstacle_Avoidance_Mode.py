from microbit import *
import machine

MOTOR_LEFT1 = pin0
MOTOR_LEFT2 = pin1
MOTOR_RIGHT1 = pin2
MOTOR_RIGHT2 = pin3

ULTRA_TRIG = pin7
ULTRA_ECHO = pin8

for pin in [MOTOR_LEFT1, MOTOR_LEFT2, MOTOR_RIGHT1, MOTOR_RIGHT2]:
    pin.set_pull(pin.PULL_UP)
    pin.write_digital(0)
ULTRA_TRIG.set_pull(ULTRA_TRIG.PULL_DOWN)
ULTRA_ECHO.set_pull(ULTRA_ECHO.PULL_DOWN)

def get_distance():
    ULTRA_TRIG.write_digital(1)
    sleep(10)
    ULTRA_TRIG.write_digital(0)
    while ULTRA_ECHO.read_digital() == 0:
        pass
    start = running_time()
    while ULTRA_ECHO.read_digital() == 1:
        pass
    end = running_time()
    distance = (end - start) * 0.034 / 2
    return distance

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

def turn_right():
    MOTOR_LEFT1.write_digital(1)
    MOTOR_LEFT2.write_digital(0)
    MOTOR_RIGHT1.write_digital(0)
    MOTOR_RIGHT2.write_digital(0)

def stop():
    for pin in [MOTOR_LEFT1, MOTOR_LEFT2, MOTOR_RIGHT1, MOTOR_RIGHT2]:
        pin.write_digital(0)

SAFE_DISTANCE = 20
while True:
    distance = get_distance()
    display.scroll(int(distance)) 
    if distance > SAFE_DISTANCE:
        forward() 
    else:
        stop()
        sleep(500)
        backward() 
        sleep(1000)
        turn_right()  
        sleep(1000)