from hub import light_matrix, button, port
import runloop
import motor
import color_sensor
import color
from app import sound

def feed_candy_1():
    return button.pressed(button.LEFT)

def feed_candy_2():
    return button.pressed(button.RIGHT)

async def main():
    # create lists
    candy1 = []
    candy2 = []

    # this makes the Game Master eat candy stick 1
    await runloop.until(feed_candy_1)
    light_matrix.clear()
    candy1.clear()
    await motor.run_for_time(port.A, 2000, -500)
    await sound.play('Bite')
    await sound.play('Bite')

    # this will read and record its sequence of colors in the list called candy 1
    for x in range(5):
        candy1.append(color_sensor.color(port.B))
        await runloop.sleep_ms(1000)
        await motor.run_for_degrees(port.A, 95, 500)

    # this makes the Game Master eat candy stick 2
    await runloop.until(feed_candy_2)
    light_matrix.clear()
    candy2.clear()
    await motor.run_for_time(port.A, 2000, -500)
    await sound.play('Bite')
    await sound.play('Bite')

    # this will read and record its sequence of colors in the list called candy 2
    for x in range(5):
        candy2.append(color_sensor.color(port.B))
        await runloop.sleep_ms(1000)
        await motor.run_for_degrees(port.A, 95, 500)

    # light up the position of red bricks if it is in the same position in both candy sticks
    candy1_red_index = -1
    if color.RED in candy1:
        candy1_red_index = candy1.index(color.RED)
    candy2_red_index = -1
    if color.RED in candy2:        
        candy2_red_index = candy2.index(color.RED)

    for x in range(5):
        print(candy1[x])

    if candy1_red_index == candy2_red_index:
        for x in range(5):
            light_matrix.set_pixel(x, candy1_red_index, 100)
            await sound.play('Win')

    else:
        light_matrix.show_image(light_matrix.IMAGE_NO)
        await sound.play('Oops')

runloop.run(main())