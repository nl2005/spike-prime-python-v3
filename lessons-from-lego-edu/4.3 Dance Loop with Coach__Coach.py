from hub import port
import runloop
import motor

async def main():
    for index in range(10):
        # Run at 250 velocity for 1/4 second
        await motor.run_for_time(port.E, 250, 300)
        await motor.run_for_time(port.F, 250, 300)

        await motor.run_for_time(port.E, 250, -300)
        await motor.run_for_time(port.F, 250, -300)

runloop.run(main())