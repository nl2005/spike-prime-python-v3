from hub import button, light_matrix, port, sound, motion_sensor
import runloop, motor_pair, motor, distance_sensor, color_sensor, color

DEFAULT_VELOCITY = 360
DEGREES_PER_CM = 360/17.5

async def main_left(): 
    await runloop.until(lambda: button.pressed(button.LEFT))
    motor_pair.unpair(motor_pair.PAIR_1)
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
    DEFAULT_VELOCITY= 10 * 30
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=DEFAULT_VELOCITY)
    await runloop.until(lambda: color_sensor.color(port.B) == color.BLACK)
    motor_pair.stop(motor_pair.PAIR_1)


async def main_right():
    await runloop.until(lambda: button.pressed(button.RIGHT))
    motor_pair.unpair(motor_pair.PAIR_1)
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
    DEFAULT_VELOCITY= 10 * 30
    while True:
        if (color_sensor.color(port.B) == color.BLACK):
            
            motor_pair.move(motor_pair.PAIR_1, 50, velocity=DEFAULT_VELOCITY)    
        else:
           
            motor_pair.move(motor_pair.PAIR_1, -50, velocity=DEFAULT_VELOCITY)
        
async def solution_right():
    await runloop.until(lambda: button.pressed(button.RIGHT))
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
    power = 30
    while True:
        if (color_sensor.reflection(port.B) < 50):
            motor_pair.move_tank(motor_pair.PAIR_1, 50, power * 10)
        else:
            motor_pair.move_tank(motor_pair.PAIR_1, power * 10, 50)


desired_power = 25
# use propertional line following
async def propertional_line_following():
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
    gain = 0.3 # 0.20
    average_white_black = 55
    while True:
        #set left power to desired_power+(gain * average_white_black-reflection)
        #set right power to desired_power-(gain * average_white_black-reflection)
        delta = gain * (average_white_black - color_sensor.reflection(port.A))
        motor_pair.move_tank(motor_pair.PAIR_1, int(10*(desired_power + delta)), int(10*(desired_power - delta)))
        
    
async def other_left():
    await runloop.until(lambda: button.pressed(button.RIGHT))
    global desired_power
    desired_power =- 10

async def other_right():
    await runloop.until(lambda: button.pressed(button.RIGHT))
    global desired_power
    desired_power =+ 10

#runloop.run(main_left(), main_right())
#runloop.run(solution_right())
runloop.run(propertional_line_following(), other_left(), other_right())
