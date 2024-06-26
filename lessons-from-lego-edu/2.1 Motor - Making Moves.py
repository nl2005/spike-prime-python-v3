import motor
from hub import port
import runloop

async def main():
    # Run a motor on port A for 360 degrees at 720 degrees per second.
    await motor.run_for_degrees(port.E, 360, 720)
    # Run a motor on port B for 360 degrees at 720 degrees per second.
    await motor.run_for_degrees(port.F, 360, 720)

runloop.run(main())