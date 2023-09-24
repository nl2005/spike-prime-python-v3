# https://education.lego.com/en-us/lessons/prime-invention-squad/broken#Planitem2
from hub import button, port
import runloop
import motor

def right_button_pressed():
    return button.pressed(button.RIGHT)

def left_button_pressed():
    return button.pressed(button.LEFT)

async def main():
    while True:
        #feed the paper
        await runloop.until(right_button_pressed)
        await motor.run_for_degrees(port.B, 1000, 500)

        #cut a square and a rectangle
        await runloop.until(left_button_pressed)
        await motor.run_for_time(port.A, 1500, -500)

        # These 4 blocks should 'cut' a square.
        await motor.run_for_degrees(port.A, 400 , 500)
        await motor.run_for_degrees(port.B, 575, 500)
        await motor.run_for_degrees(port.A, -400 , 500)
        await motor.run_for_degrees(port.B, -575, 500)

        # These 4 blocks should 'cut' a rectangle.
        await motor.run_for_degrees(port.A, -60, 500)
        await motor.run_for_degrees(port.B, -800, 500)
        await motor.run_for_degrees(port.A, 400, 500)
        await motor.run_for_degrees(port.B, 1600, 500)
        await motor.run_for_degrees(port.A, -400, 500)
        await motor.run_for_degrees(port.B, -800, 500)

runloop.run(main())