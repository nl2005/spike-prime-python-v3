import runloop
import motor
import color_sensor
import color
from hub import port, light_matrix

color_value = color_sensor.color(port.D)
def diffirent_color():
    return color_sensor.color(port.D) not in (-1, color_value)

async def main():
    global color_value
    color_value = color_sensor.color(port.D)


# NL note: use lambda here because the function need access to color_value, which is not avaiable until main runs. 
    while True:
        # lambda: color_sensor.color(port.D) not in (-1, color_value))
        color_value = color_sensor.color(port.D)
        await runloop.until(diffirent_color)
        

        #if senses blue the arms will move
        if color_value == color.BLUE:
            light_matrix.show_image(light_matrix.IMAGE_HAPPY)
            await motor.run_for_degrees(port.A, 360, 400)

        #if senses green the legs will move
        elif color_value == color.GREEN:
            light_matrix.show_image(3)
            await motor.run_for_degrees(port.B, 360, 600)

        #if senses yellow both arms and legs will move together slowly
        elif color_value == color.YELLOW:
            light_matrix.show_image(light_matrix.IMAGE_HAPPY)
            motor.run_for_degrees(port.A, 360, 200)
            motor.run_for_degrees(port.B, 360, 400)

        #if senses red both arms and legs will move together quickly
        elif color_value == color.RED:
            light_matrix.show_image(light_matrix.IMAGE_HAPPY)
            motor.run_for_degrees(port.A, 360, 600)
            motor.run_for_degrees(port.B, 360, 800)

        #if senses any other color or no color
        else:
            light_matrix.show_image(light_matrix.IMAGE_SAD)

runloop.run(main())