from hub import port, light_matrix
import runloop
import distance_sensor
import force_sensor

def is_force_sensor_pressed():
    # collect input from force sensor
    return force_sensor.pressed(port.B)

def is_force_sensor_released():
    # collect input from force sensor
    return not force_sensor.pressed(port.B)

async def main():
    runloop.until(is_force_sensor_pressed)
    await light_matrix.write('JUMP!')

    runloop.until(is_force_sensor_released)
    dist_cm = distance_sensor.distance(port.F)/10
    print(str(dist_cm) + ' cm')

runloop.run(main())
#Part 2: Create your list
'''
from hub import port, light_matrix
import runloop
import force_sensor

def is_force_sensor_pressed():
    # collect input from force sensor
    return force_sensor.pressed(port.B)

async def main():

    # create a list for each person using the values from the table
    name1 = [trial1, trial2, trial3]
    name2 = [trial1, trial2, trial3]

    # print the maximum value from each person's list
    print('Name 1: ' + str(max(name1)))
    print('Name 2: ' + str(max(name2)))

    # display the max values on the hub when the force sensor is pressed
    await runloop.until(is_force_sensor_pressed)
    await light_matrix.write(str(max(name1)))
    await runloop.sleep_ms(2000)
    light_matrix.show_image(light_matrix.IMAGE_YES)
    await runloop.sleep_ms(1000)
    await light_matrix.write(str(max(name2)))
    await runloop.sleep_ms(2000)
    light_matrix.show_image(light_matrix.IMAGE_YES)

runloop.run(main())

from hub import port, light_matrix
import runloop
import force_sensor

def is_force_sensor_pressed():
    # collect input from force sensor
    return force_sensor.pressed(port.B)

async def main():
    # create a list for each person using the values from the table
    name1 = [trial1, trial2, trial3]
    name2 = [trial1, trial2, trial3]

    # print the maximum value from each person's list
    print('Name 1: ' + str(max(name1)))
    print('Name 2: ' + str(max(name2)))

    # combine the lists when the force sensor is pressed
    # display the sum of the new list
    await runloop.until(is_force_sensor_pressed)
    combo_list = name1 + name2
    print(combo_list)
    await light_matrix.write(str(sum(combo_list)))
    print(sum(combo_list))
    light_matrix.show_image(light_matrix.IMAGE_YES)

runloop.run(main())
'''