from microbit import *
import machine

# 定义电机控制引脚（需根据实际接线调整）
MOTOR_LEFT1 = pin0
MOTOR_LEFT2 = pin1
MOTOR_RIGHT1 = pin2
MOTOR_RIGHT2 = pin3

# 初始化引脚为输出模式
pins = [MOTOR_LEFT1, MOTOR_LEFT2, MOTOR_RIGHT1, MOTOR_RIGHT2]
for pin in pins:
    pin.set_pull(pin.PULL_UP)
    pin.write_digital(0)

def motor_forward():
    """控制电机正转，实现机器人前进"""
    MOTOR_LEFT1.write_digital(1)
    MOTOR_LEFT2.write_digital(0)
    MOTOR_RIGHT1.write_digital(1)
    MOTOR_RIGHT2.write_digital(0)

def motor_stop():
    """控制电机停止转动"""
    for pin in [MOTOR_LEFT1, MOTOR_LEFT2, MOTOR_RIGHT1, MOTOR_RIGHT2]:
        pin.write_digital(0)

# 主程序：前进3秒后停止
while True:
    motor_forward()
    sleep(3000)  # 持续前进3秒
    motor_stop()
    sleep(1000)  # 停止1秒后循环