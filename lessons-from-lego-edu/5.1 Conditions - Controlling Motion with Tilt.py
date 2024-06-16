from hub import light_matrix, motion_sensor
import runloop
from app import sound

def if_tapped():
    # If the hub is tapped, return the TAPPED gesture
    return motion_sensor.gesture() == motion_sensor.TAPPED

async def run_tapped():
#Wait until the hub is tapped to show a sad face
    await runloop.until(if_tapped)
    light_matrix.show_image(light_matrix.IMAGE_SAD)
    print('Stop Please')


def face_up():
    # Return if the hub is oriented USB port up
    '''
    The speaker side is motion_sensor.FRONT
    The USB side is motion_sensor.BACK
    The A, C, E port side is motion_sensor.LEFT
    The B, D, F port side is motion_sensor.RIGHT
    The light matrix side is motion_sensor.TOP
    The battery side is motion_sensor.BOTTOM
    '''
    return motion_sensor.up_face() == motion_sensor.BACK

async def run_face_up():
    await runloop.until(face_up)
    light_matrix.show_image(light_matrix.IMAGE_ARROW_N)
    print('I am awake')
    await sound.play('Applause 1')


async def main():
    await run_tapped()
    await run_face_up()

runloop.run(main())