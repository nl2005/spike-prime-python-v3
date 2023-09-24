from hub import port
import runloop
import color_sensor
import color
from app import sound

async def main():
    #if the color sensor senses blue, it will play bird sound
    if color_sensor.color(port.A) == color.BLUE:
        await sound.play('Bird')
        print('Blue Detected')


    #if the color sensor senses green, it will play cat angry sound
    elif color_sensor.color(port.A) == color.GREEN:
        await sound.play('Cat Angry')
        print('Green Detected')


    #if the color sensor senses red, it willplay snoring sound
    elif color_sensor.color(port.A) == color.RED:
        await sound.play('Snoring')
        print('Red Detected')


    #if the color sensor senses magenta, it will play moo sound
    elif color_sensor.color(port.A) == color.MAGENTA:
        await sound.play('Moo')
        print('Magenta Detected')


    #if the color sensor sesnes yellow, it will play wobble sound
    elif color_sensor.color(port.A) == color.YELLOW:
        await sound.play('Wobble')
        print('Yellow Detected')


    #if the color sensor does not sense any of these colors, it will play dog bark 1 sound
    else:
        await sound.play('Dog Bark 1')
        print('What happened?')

runloop.run(main())