from hub import port, light_matrix, button
import runloop
import motor_pair, motor

async def main():
    driving_velocity = 250

    # pair motors
    motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)

    # define the ride function
    async def ride():
        await light_matrix.write(str(driving_velocity))
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, 720, 0, velocity = driving_velocity)

    # set conditions for moving forward and setting velocity
    while True:
        if button.pressed(button.LEFT):
            driving_velocity -= 50
            await ride()
            await runloop.sleep_ms(3000)
        elif button.pressed(button.RIGHT):
            driving_velocity += 50
            await ride()
            await runloop.sleep_ms(3000)

async def main2():
    # define the initial driving velocity
    driving_velocity = 250
    # defining the turn distance
    turning_left = -360
    turning_right = 360

    # pair motors
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)

    # define the ride and turn functions
    async def ride():
        await light_matrix.write(str(driving_velocity))
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, 720, 0, velocity = driving_velocity)

    async def turn_left():
        await light_matrix.write(str(turning_left/4))
        await motor.run_for_degrees(port.C, turning_left, 250)

    async def turn_right():
        await light_matrix.write(str(turning_right/4))
        await motor.run_for_degrees(port.D, turning_right, 250)

    # set conditions for moving forward and setting velocity
    while True:
        await ride()
        if button.pressed(button.LEFT):
            driving_velocity -= 50
            turning_left -= 360
            await turn_left()
            await runloop.sleep_ms(3000)

        elif button.pressed(button.RIGHT):
            driving_velocity += 50
            turning_right += 360
            await turn_right()
            await runloop.sleep_ms(3000)



runloop.run(main())