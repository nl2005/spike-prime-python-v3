from hub import port
import runloop
import color_sensor
import motor
import color
from app import sound

async def main():
    await motor.run_to_absolute_position(port.A, 0, 500)
    await motor.run_to_absolute_position(port.F, 240, 500)
    await motor.run_to_absolute_position(port.A, 90, 500)
    await motor.run_to_absolute_position(port.F, 25, 500)

    await check_color()

    await motor.run_to_absolute_position(port.A, 0, 500)
    await motor.run_to_absolute_position(port.F, 240, 500)
    await motor.run_to_absolute_position(port.A, 270, 500)
    await motor.run_to_absolute_position(port.F, 25, 500)

    await check_color()

    await motor.run_to_absolute_position(port.A, 0, 500)
    await motor.run_to_absolute_position(port.F, 240, 500)

async def check_color():
    await motor.run_to_absolute_position(port.F, 235, 500)

    if color_sensor.color(port.D) is color.MAGENTA:
        await motor.run_to_absolute_position(port.A, 0, 500)
        await motor.run_to_absolute_position(port.F, 25, 500)
        await sound.play('Triumph')
        await motor.run_to_absolute_position(port.F, 240, 500)
    else:
        await sound.play('Oops')
        await motor.run_to_absolute_position(port.F, 25, 500)
        for x in range(3):
            await motor.run_for_degrees(port.F, -100, 1000)
            await motor.run_for_degrees(port.F, 100, 1000)

runloop.run(main())