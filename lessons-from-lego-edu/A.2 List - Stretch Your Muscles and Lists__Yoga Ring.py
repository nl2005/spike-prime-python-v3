from hub import motion_sensor, light_matrix
import runloop
import random

async def main():
    # Create a list with the hub's orientation
    yoga_moves = [motion_sensor.FRONT, motion_sensor.BACK, motion_sensor.LEFT, motion_sensor.RIGHT]
    random_move = random.choice(yoga_moves)

    # Follow this routine
    print('LEFT')
    print('RIGHT')
    print(random_move)
    print('BACK')
    print('FRONT')
    print(random_move)
    print('READY GO!')

    orientation = motion_sensor.up_face()

    while True:
        await runloop.until(lambda: motion_sensor.up_face() != orientation)
        orientation = motion_sensor.up_face()

        if orientation == yoga_moves[2]:
            print('Left Side')
            light_matrix.show_image(light_matrix.IMAGE_ARROW_W)
        elif orientation == yoga_moves[3]:
            print('Right Side')
            light_matrix.show_image(light_matrix.IMAGE_ARROW_E)
        elif orientation == random_move:
            print('Random')
            light_matrix.show_image(light_matrix.IMAGE_SILLY)
        elif orientation == yoga_moves[1]:
            print('Back')
            light_matrix.show_image(light_matrix.IMAGE_ARROW_N)
        elif orientation == yoga_moves[0]:
            print('Front')
            light_matrix.show_image(light_matrix.IMAGE_ARROW_S)

runloop.run(main())