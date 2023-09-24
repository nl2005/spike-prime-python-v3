import runloop
import motor
import force_sensor
from hub import port

def is_force_sensor_pressed():
    # collect input from force sensor
    return force_sensor.pressed(port.F)

def is_force_sensor_not_pressed():
    # collect input from force sensor
    return not force_sensor.pressed(port.F)

async def main():
    # wait until the force sensor is pressed
    await runloop.until(is_force_sensor_pressed)

    motor.run(port.A, 750)
    # wait until the force sensor is not pressed
    await runloop.until(is_force_sensor_not_pressed)

    motor.stop(port.A)

    await runloop.sleep_ms(2000)
    # turn on motor
    motor.run(port.A, 1000)

    # wait until the force sensor is pressed
    await runloop.until(is_force_sensor_pressed)

    # stop motor
    motor.stop(port.A)


runloop.run(main())