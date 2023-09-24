from hub import button, light_matrix, port, sound, motion_sensor
import runloop, motor_pair

DEFAULT_VELOCITY = 500
DEGREES_PER_CM = 360/17.5

async def main(): 
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D) 
    await runloop.sleep_ms(1000)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(20 * DEGREES_PER_CM), 0, velocity=-DEFAULT_VELOCITY)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(20 * DEGREES_PER_CM), 0, velocity=-DEFAULT_VELOCITY)

    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 20 * 360, -40, velocity=DEFAULT_VELOCITY)

    motion_sensor.reset_yaw(0)
    
    motor_pair.move(motor_pair.PAIR_1, 100, velocity=DEFAULT_VELOCITY)
    await runloop.until(lambda: -motion_sensor.tilt_angles()[0]/10 > 90)
    motor_pair.stop(motor_pair.PAIR_1)

    motor_pair.move(motor_pair.PAIR_1, -100, velocity=DEFAULT_VELOCITY)
    await runloop.until(lambda: -motion_sensor.tilt_angles()[0]/10 <0)
    motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())
