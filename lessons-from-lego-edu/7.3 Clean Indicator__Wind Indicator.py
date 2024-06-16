from hub import port, button
import runloop
import motor
import color_sensor
import color

# define function for reporting the clean level
def report(height, color):
    runloop.run(motor.run_to_absolute_position(port.E, height, 500))
    print('Clean Level', color)

async def main():
    while True:
        await runloop.until(lambda: button.pressed(button.LEFT)>0)
        #when sensing a color, the height is set
        if color_sensor.color(port.B) is color.RED:
            report(70, 'Red')
        elif color_sensor.color(port.B) is color.YELLOW:
            report(60, 'Yellow')
        elif color_sensor.color(port.B) is color.BLUE:
            report(50, 'Blue')
        elif color_sensor.color(port.B) is color.GREEN:
            report(25, 'Green')
        #if it doesn't sense a color, it moves to the 0 position
        else:
            await motor.run_to_absolute_position(port.E, 0, 1000)
            print("No Reading")

runloop.run(main())