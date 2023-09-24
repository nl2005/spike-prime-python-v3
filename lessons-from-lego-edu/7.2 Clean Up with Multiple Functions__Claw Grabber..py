from hub import port
import runloop
import motor
import force_sensor

def is_pressed():
    return force_sensor.pressed(port.E)

def is_released():
    return not force_sensor.pressed(port.E)

async def grab_and_release(grip):
    await runloop.until(is_pressed)
    # motor will close grabber
    await motor.run_to_absolute_position(port.A, 345, grip, direction=motor.COUNTERCLOCKWISE )
    await runloop.until(is_released)
    # motor will release grabber
    await motor.run_to_absolute_position(port.A, 25, grip)

async def main():
    while True:
        await grab_and_release(1000)

runloop.run(main())