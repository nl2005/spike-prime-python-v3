from hub import port, light_matrix
import runloop
import motor_pair

async def main():
    # Countdown
    await light_matrix.write("3")
    await runloop.sleep_ms(1000)
    await light_matrix.write("2")
    await runloop.sleep_ms(1000)
    await light_matrix.write("1")
    await runloop.sleep_ms(1000)

    # Pair motors on port A and B
    motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)

    # Move straight at default velocity for 5 second
    await motor_pair.move_for_time(motor_pair.PAIR_1, 500, 0, velocity=200)

     # Turn for different amounts
    await motor_pair.move_for_time(motor_pair.PAIR_1, 1000, -20, velocity=280)
    await motor_pair.move_for_time(motor_pair.PAIR_1, 1000, 90, velocity=280)
    await motor_pair.move_tank_for_time(motor_pair.PAIR_1, 500, 100, 200)

runloop.run(main())