
from microbit import *
c = 0
b= 0
number = 0
direction = "RIGHT"

def turnL(a: number):
    motobit.enable(MotorPower.ON)
    motobit.set_motor_speed(Motor.LEFT, MotorDirection.REVERSE, 40)
    motobit.set_motor_speed(Motor.RIGHT, MotorDirection.REVERSE, 40)
    pause(a)
    motobit.enable(MotorPower.OFF)

def on_button_pressed_a():
    motobit.enable(MotorPower.OFF)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    c = input.acceleration(Dimension.X)
    move(51, 7000)
    turnR(590)
    move(51, 4700)
    turnL(590)
    move(51, 4700)
    turnR(590)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def move(e: number, d: number):
    while(abs(c - number)>=10):
            number = input.acceleration(Dimension.X)
            if(number<=c):
                motobit.enable(MotorPower.OFF)
                motobit.enable(MotorPower.ON)
                motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 5)
                if(abs(c - number)<=10):
                    motobit.enable(MotorPower.OFF)
                    break
                    #while loop to make it continuious so it adds on
            elif(number>=c):
                motobit.enable(MotorPower.OFF)
                motobit.enable(MotorPower.ON)
                motobit.set_motor_speed(Motor.RIGHT, MotorDirection.REVERSE, 5)
                if(abs(c - number)>=10):
                    motobit.enable(MotorPower.OFF)
                    break
                    #while loop to make it continuious so it adds on
            
    motobit.enable(MotorPower.ON)
    motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 64)
    motobit.set_motor_speed(Motor.RIGHT, MotorDirection.REVERSE, e)
    pause(d)
    motobit.enable(MotorPower.OFF)
    
def turnR(b: number):
    motobit.enable(MotorPower.ON)
    motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 40)
    motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 40)
    motobit.enable(MotorPower.OFF)

def on_forever():
    pause(10000)
    
    


basic.forever(on_forever)

    
    
    