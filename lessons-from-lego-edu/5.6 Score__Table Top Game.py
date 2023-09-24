import runloop, motor
from hub import port, light_matrix, button

def right_released():
    return not button.pressed(button.RIGHT)

def left_released():
    return not button.pressed(button.LEFT)

async def main():
    # Run a motor on port A to 180 degrees at 720 degrees per second. This will put the arm up to be ready to swing.
    await motor.run_to_absolute_position(port.A, 180, 720)

    # Run a motor on port A for 360 degrees at 720 degrees per second.
    await motor.run_for_degrees(port.A, 360, 720)

    #set the score to 0.
    score = 0

    #Loop conditional statement to indicate score
    while True:
        if button.pressed(button.RIGHT):
            await runloop.until(right_released)
            light_matrix.show_image(light_matrix.IMAGE_HAPPY)
            score += 1
            print(score)

        elif button.pressed(button.LEFT):
            await runloop.until(left_released)
            light_matrix.show_image(light_matrix.IMAGE_SAD)
            print('0')

runloop.run(main())
