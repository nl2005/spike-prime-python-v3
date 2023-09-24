from hub import light_matrix, port, motion_sensor, sound
import runloop, motor, motor_pair, color_sensor, color

DEFAULT_VELOCITY = 360

#def delta_follow_line

async def main():
    # calibrate
    await motor.run_for_degrees(port.E, -360, 360)
    motor.reset_relative_position(port.E, 0)
    await motor.run_to_relative_position(port.E, 140, 750)

    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
    
    motion_sensor.reset_yaw(0)
    speed = 30*10
    await runloop.sleep_ms(1000)

    # start out move until see black
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 360, 0)
    motor_pair.move(motor_pair.PAIR_1, -30)
    await runloop.until(lambda: color_sensor.color(port.B) == color.BLACK)
    
    # follow line until 44 degree. 
    # note value is negative 10th of degree compare to word block
    while (-motion_sensor.tilt_angles()[0]/10 < 44):
        if color_sensor.reflection(port.B) < 50 : 
            motor_pair.move_tank(motor_pair.PAIR_1, speed, 0)
        else:
            motor_pair.move_tank(motor_pair.PAIR_1, 0, speed)
    motor_pair.stop(motor_pair.PAIR_1)
    await runloop.sleep_ms(1000)

    # turn left until facing west
    motor_pair.move(motor_pair.PAIR_1, -100)
    await runloop.until(lambda: -motion_sensor.tilt_angles()[0]/10 < -89)
    motor_pair.stop(motor_pair.PAIR_1)

    # move straight a little
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 6, 0) # velocity=DEFAULT_VELOCITY
    
    # turn left until see black 
    motor_pair.move(motor_pair.PAIR_1, -30)
    await runloop.until(lambda: color_sensor.color(port.B) == color.BLACK)
    motor_pair.stop(motor_pair.PAIR_1)

    # turn right until -46 deg (north west)
    motor_pair.move_tank(motor_pair.PAIR_1, 500, 0)
    await runloop.until(lambda: -motion_sensor.tilt_angles()[0]/10 > -46)
    motor_pair.stop(motor_pair.PAIR_1)

    # move forward until see black line
    motor_pair.move(motor_pair.PAIR_1, 0)
    await runloop.until(lambda: color_sensor.color(port.B) == color.BLACK)

    # lower stick
    await motor.run_to_relative_position(port.E, 55, 500)

    # hit screen changer
    for i in range (3):
        # back to black
        motor_pair.move(motor_pair.PAIR_1, 0, velocity=-360)
        await runloop.until(lambda: color_sensor.color(port.B) == color.BLACK)
        motor_pair.stop(motor_pair.PAIR_1)

        # push
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(360*0.7), 0)
        motor_pair.stop(motor_pair.PAIR_1)

    # lift expert
    await motor.run_to_relative_position(port.E, 140, 750)

    # back to black
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=-360)
    await runloop.until(lambda: color_sensor.color(port.B) == color.BLACK)
    motor_pair.stop(motor_pair.PAIR_1)

    # turn left until -170 (facing south)
    motor_pair.move_tank(motor_pair.PAIR_1, -500, 500)
    await runloop.until(lambda: -motion_sensor.tilt_angles()[0]/10 <-170)
    motor_pair.stop(motor_pair.PAIR_1)

    # back to home
    await motor_pair.move_for_degrees(motor_pair.PAIR_1,  360*3, 0)
    



runloop.run(main())
