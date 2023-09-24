from hub import port
import runloop
import motor_pair

async def main():
    # Pair motors on port A and B
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.B)

    # Move straight at 500 velocity
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=500)

runloop.run(main())