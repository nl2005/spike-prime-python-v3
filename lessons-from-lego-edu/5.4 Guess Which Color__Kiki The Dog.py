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
    #if the color sensor does not sense blue, it will play dog bark 1 sound
    else:
        await sound.play('Dog Bark 1')
        print('What happened?')

runloop.run(main())