import runloop
import motor_pair, force_sensor
from hub import port

def is_force_sensor_pressed():
    # collect input from force sensor
    return force_sensor.pressed(port.F)

async def main():
    # pair motors with the left motor on port B and right motor on port A
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
    # move motor pair straight forward
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=-450)

     # wait until the force sensor is pressed
    await runloop.until(is_force_sensor_pressed)

    # stop the rhino
    motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())