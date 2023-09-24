from hub import port, button
import runloop
import motor

def pressed():
    # When the left button is pressed, it returns to open
    return button.pressed(button.LEFT)

def released():
    # When the left button is released, it returns to close
    return not button.pressed(button.LEFT)

async def main():
    while True:
        await runloop.until(pressed)
        motor.run(port.F, -750)
        await runloop.until(released)
        motor.run(port.F, 750)

runloop.run(main())