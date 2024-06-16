# https://education.lego.com/en-us/lessons/prime-invention-squad/broken#Planitem2
from hub import button, port
import runloop
import motor

def right_button_pressed():
    return button.pressed(button.RIGHT)>0

def left_button_pressed():
    return button.pressed(button.LEFT)>0

async def main():
    while True:
        #feed the paper
        await runloop.until(right_button_pressed)
        await motor.run_for_degrees(port.F, 1000, 500)

        #cut a square and a rectangle
        await runloop.until(left_button_pressed)
        await motor.run_for_time(port.E, 1500, -500)

        # These 4 blocks should 'cut' a square.
        await motor.run_for_degrees(port.E, 400 , 500)
        await motor.run_for_degrees(port.F, 575, 500)
        await motor.run_for_degrees(port.E, -400 , 500)
        await motor.run_for_degrees(port.F, -575, 500)

        # These 4 blocks should 'cut' a rectangle.
        await motor.run_for_degrees(port.E, -60, 500)
        await motor.run_for_degrees(port.F, -800, 500)
        await motor.run_for_degrees(port.E, 400, 500)
        await motor.run_for_degrees(port.F, 1600, 500)
        await motor.run_for_degrees(port.E, -400, 500)
        await motor.run_for_degrees(port.F, -800, 500)

runloop.run(main())