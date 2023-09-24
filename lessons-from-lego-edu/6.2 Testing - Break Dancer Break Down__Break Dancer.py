from hub import light_matrix
import runloop

async def main():
    # show a heart
    light_matrix.show_image(light_matrix.IMAGE_HEART)
    

runloop.run(main())