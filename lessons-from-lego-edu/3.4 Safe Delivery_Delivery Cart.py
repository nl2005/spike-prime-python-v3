import motor_pair
import runloop
import distance_sensor
import motor
from hub import port

def distance_sensor_closer_than():
        #return if the distance sensor is less than 150 mm
    distance = distance_sensor.distance(port.A)
    return distance < 150 and distance > -1
async def main():
    # Pair motors on port A and B
    motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)

    # Move the rear motor to the 0 degree position to make the cart move straight
    await motor.run_to_absolute_position(port.F, 0, 250)

    # start motor pair moving
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=200)

    # wait until the distance sensor is clower than 150 mm
    await runloop.until(distance_sensor_closer_than)

    # The cart will stop when the distance is less than 150 mm.
    motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())