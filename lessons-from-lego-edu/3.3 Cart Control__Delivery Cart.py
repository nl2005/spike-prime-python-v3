import runloop
import motor_pair
import distance_sensor
from hub import port

def distance_sensor_greater_than():
    # return if the distance sensor is greater than 150 mm
    distance = distance_sensor.distance(port.A)
    return distance == -1 or distance > 150

def distance_sensor_less_than():
    #return if the distance sensor is less than 100 mm
    distance = distance_sensor.distance(port.A)
    return distance < 100 and distance > -1

async def main():
    # pair motors
    motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)

    # wait until the distance sensor reads more than 150 mm
    await runloop.until(distance_sensor_greater_than)    # turn on motor pair
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=500)

    # wait until the distance sensor reads less than 50 mm
    await runloop.until(distance_sensor_less_than)

    # stop motor
    motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())