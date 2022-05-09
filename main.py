e=0
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
    e = input.compass_heading()
    move(7000)
    turnR(590)
    move(4700)
    turnL(590)
    move(4700)
    turnR(590)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def move(d: number):
    c = 0
    while e!=d:
        number2 = input.compass_heading()
        if number2 <= c:
            while(abs(c - number2) >= 10):
                motobit.enable(MotorPower.OFF)
                motobit.enable(MotorPower.ON)
                motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 5)
                if abs(c - number2) >= 10:
                    break
                    motobit.enable(MotorPower.ON)
        elif number2 >= c:
            while(abs(c - number2) >= 10):
                motobit.enable(MotorPower.OFF)
                motobit.enable(MotorPower.ON)
                motobit.set_motor_speed(Motor.RIGHT, MotorDirection.REVERSE, 5)
                if abs(c - number2) >= 10:
                    break
                    motobit.enable(MotorPower.ON)
        else:
            motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 64)
            motobit.set_motor_speed(Motor.RIGHT, MotorDirection.REVERSE, 64)
            pause(d/5)
            e= e+d/5
            motobit.enable(MotorPower.OFF)
    
        
    
    # while loop to make it continuious so it adds on
    motobit.enable(MotorPower.ON)
    motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 64)
    motobit.set_motor_speed(Motor.RIGHT, MotorDirection.REVERSE, 64)
    pause(d)
    motobit.enable(MotorPower.OFF)
def turnR(b: number):
    motobit.enable(MotorPower.ON)
    motobit.set_motor_speed(Motor.LEFT, MotorDirection.FORWARD, 40)
    motobit.set_motor_speed(Motor.RIGHT, MotorDirection.FORWARD, 40)
    motobit.enable(MotorPower.OFF)
f = 0
g = 0
number = 0
direction = "RIGHT"

def on_forever():
    pause(10000)
basic.forever(on_forever)
