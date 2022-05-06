let c = 0
let b = 0
let number = 0
let direction = "RIGHT"
function turnL(a: number) {
    motobit.enable(MotorPower.On)
    motobit.setMotorSpeed(Motor.Left, MotorDirection.Reverse, 40)
    motobit.setMotorSpeed(Motor.Right, MotorDirection.Reverse, 40)
    pause(a)
    motobit.enable(MotorPower.Off)
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    motobit.enable(MotorPower.Off)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    let c = input.acceleration(Dimension.X)
    move(51, 7000)
    turnR(590)
    move(51, 4700)
    turnL(590)
    move(51, 4700)
    turnR(590)
})
function move(e: number, d: number) {
    let number: number;
    while (Math.abs(c - number) >= 10) {
        number = input.acceleration(Dimension.X)
        if (number <= c) {
            motobit.enable(MotorPower.Off)
            motobit.enable(MotorPower.On)
            motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, 5)
            if (Math.abs(c - number) <= 10) {
                motobit.enable(MotorPower.Off)
                break
            }
            
        } else if (number >= c) {
            // while loop to make it continuious so it adds on
            motobit.enable(MotorPower.Off)
            motobit.enable(MotorPower.On)
            motobit.setMotorSpeed(Motor.Right, MotorDirection.Reverse, 5)
            if (Math.abs(c - number) >= 10) {
                motobit.enable(MotorPower.Off)
                break
            }
            
        }
        
    }
    // while loop to make it continuious so it adds on
    motobit.enable(MotorPower.On)
    motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, 64)
    motobit.setMotorSpeed(Motor.Right, MotorDirection.Reverse, e)
    pause(d)
    motobit.enable(MotorPower.Off)
}

function turnR(b: number) {
    motobit.enable(MotorPower.On)
    motobit.setMotorSpeed(Motor.Left, MotorDirection.Forward, 40)
    motobit.setMotorSpeed(Motor.Right, MotorDirection.Forward, 40)
    motobit.enable(MotorPower.Off)
}

basic.forever(function on_forever() {
    pause(10000)
})
