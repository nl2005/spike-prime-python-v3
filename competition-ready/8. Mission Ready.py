from hub import button, light_matrix, port, sound, motion_sensor
import runloop, motor_pair, motor


DEFAULT_VELOCITY = 500
DEGREES_PER_CM = 360/27.63 #17.5


async def main(): 
    
    await motor.run_for_time(port.D, 1000, -750)
    await motor.run_for_time(port.C, 750,-750)
    await motor.run_for_degrees(port.C, int(0.25 * 360), 750)

    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(25 * DEGREES_PER_CM), -250)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(12 * DEGREES_PER_CM), 250)
    await motor.run_for_degrees(port.C, 180, 750)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(7 * DEGREES_PER_CM), -250)

    await motor.run_for_time(port.C, 1000,-750)
    await motor.run_for_degrees(port.C, 360, 750)

    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(10 * DEGREES_PER_CM), 0, velocity=250)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 150, -100, velocity=250)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 4*360, -10, velocity=250)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(25 * DEGREES_PER_CM), 0, velocity=250)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 150, -100, velocity=250)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(64*DEGREES_PER_CM), 0, velocity=250)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 150, -100, velocity=250)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(25*DEGREES_PER_CM), 0, velocity=250)

    await motor.run_for_degrees(port.D, 90, 750)

    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(25*DEGREES_PER_CM), 0, velocity=-250)

runloop.run(main())
