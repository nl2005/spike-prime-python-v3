import motor
from hub import port
import runloop

async def main():
    # Run a motor on port A for 360 degrees at 720 degrees per second.
    await motor.run_for_degrees(port.E, 360, 720)

    # Run a motor on port A to 0 degrees at 720 degrees per second.
    await motor.run_to_absolute_position(port.E, 0, 720)

    # Run a motor on port A to 0 degrees at 720 degrees per second. Then it will wait 2 seconds and move to 90 degrees in the clockwise direction.
    await motor.run_to_absolute_position(port.E, 0, 720)
    await runloop.sleep_ms(2000)
    await motor.run_to_absolute_position(port.E, 90, 720, direction=motor.CLOCKWISE)

runloop.run(main())