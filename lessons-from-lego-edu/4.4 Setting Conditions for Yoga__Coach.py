from hub import port
import runloop
import motor

async def main():
    count = 0
    #run motors when count is less than 5
    while count < 3:
    # Run at 250 velocity for 1 second
        await motor.run_for_time(port.B, 1000, 250)
        await motor.run_for_time(port.A, 1000, 250)

        await motor.run_for_time(port.B, 1000, -250)
        await motor.run_for_time(port.A, 1000, -250)

        count += 1

runloop.run(main())