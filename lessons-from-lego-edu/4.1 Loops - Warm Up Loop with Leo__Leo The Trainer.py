from hub import port
import motor_pair
import runloop

async def main():
    # Pair motors on port A and B
    motor_pair.pair(motor_pair.PAIR_1, port.B, port.A)

    for index in range(5):
        await motor_pair.move_for_time(motor_pair.PAIR_1, 500 ,0, velocity = 500)
        await runloop.sleep_ms(500)
        await motor_pair.move_for_time(motor_pair.PAIR_1, 500 ,0, velocity = -500)
        await runloop.sleep_ms(500)

runloop.run(main())