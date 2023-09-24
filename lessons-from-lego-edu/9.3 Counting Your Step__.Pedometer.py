from hub import light_matrix, motion_sensor, button
import runloop

async def main():
    step = 0
    # reset the yaw angle to 0
    motion_sensor.reset_yaw(0)
    await light_matrix.write('Walk!')

    while True:
        # get the tilt values
        tilt = motion_sensor.tilt_angles()
        # store the yaw value from the tilt tuple
        yaw = tilt[0]

        if yaw > 75:
            step += 1
        elif yaw <-75:
            step += 1
        elif button.pressed(button.LEFT):
            await light_matrix.write(str(step))
            break

runloop.run(main())