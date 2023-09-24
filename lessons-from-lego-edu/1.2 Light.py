from hub import light_matrix
import runloop

async def main():
    # show a heart
    light_matrix.show_image(light_matrix.IMAGE_HEART)
    await runloop.sleep_ms(5000)
    light_matrix.clear()

    # show a happy face
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)
    await runloop.sleep_ms(5000)
    light_matrix.clear()

runloop.run(main())