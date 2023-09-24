from hub import button, light_matrix, port, sound, motion_sensor
import runloop, motor_pair, motor, distance_sensor

DEFAULT_VELOCITY = 360
DEGREES_PER_CM = 360/17.5

async def main(): 
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
    global DEFAULT_VELOCITY
    DEFAULT_VELOCITY= 10 * 30
    global DEGREES_PER_CM
    DEGREES_PER_CM = 360 / 17.5 
    await motor.run_for_time(port.E,1000, 200)
    await motor.run_for_time(port.E,1000,-200)
    # https://en.wikipedia.org/wiki/Piano_key_frequencies
    await sound.beep(440,200)
    await sound.beep(1661,200)

async def main_left():
    while True:
        await runloop.until(lambda: button.pressed(button.LEFT)>0)
        await runloop.sleep_ms(1000)
        await motor_pair.move_for_degrees(motor_pair.PAIR_1,int(DEGREES_PER_CM * 20),0, velocity=DEFAULT_VELOCITY)

async def main_right():
    while True:
        await runloop.until(lambda: button.pressed(button.RIGHT)>0)
        await runloop.sleep_ms(1000)
        motor_pair.move(motor_pair.PAIR_1, 0, velocity=DEFAULT_VELOCITY)
        await runloop.until(lambda: distance_sensor.distance(port.F) < 100)
        motor_pair.stop(motor_pair.PAIR_1)


async def solution():
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
    global DEFAULT_VELOCITY
    DEFAULT_VELOCITY= 10 * 30
    global DEGREES_PER_CM
    DEGREES_PER_CM = 360 / 17.5
    await motor.run_for_time(port.E,1000, -200)
    await motor.run_for_degrees(port.E,75,200)
    await sound.beep(440,200)
    await sound.beep(1661,200)

async def solution_right():
    await runloop.until(lambda: button.pressed(button.RIGHT)>0)
    await runloop.sleep_ms(1000)
    motor_pair.move(motor_pair.PAIR_1, 0, velocity=DEFAULT_VELOCITY)
    runloop.until(lambda: distance_sensor.distance(port.F) < 100)
    motor_pair.stop(motor_pair.PAIR_1)
    await motor.run_for_degrees(port.E, 75, DEFAULT_VELOCITY)
    await sound.beep(440,200)
    await sound.beep(1661,200)
    motor_pair.move_for_degrees(motor_pair.PAIR_1, -int(DEGREES_PER_CM*20),0)


async def other():
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
    global DEFAULT_VELOCITY
    DEFAULT_VELOCITY= 10 * 30
    global DEGREES_PER_CM
    DEGREES_PER_CM = 360 / 17.5
    await motor.run_for_time(port.E,1000, 200)
    await motor.run_for_time(port.E,1000, -200)
    await motor.run_for_degrees(port.E,75,200)
    await sound.beep(440,200)
    await sound.beep(1661,200)

async def other_right():
    await runloop.until(lambda: button.pressed(button.RIGHT)>0)
    distance = 250
    await runloop.sleep_ms(1000)
    for i in range(4):
        motor_pair.move(motor_pair.PAIR_1, 0, velocity=DEFAULT_VELOCITY)
        await runloop.until(lambda: distance_sensor.distance(port.F) < distance)
        motor_pair.stop(motor_pair.PAIR_1)
        await motor.run_for_degrees(port.E, 75, DEFAULT_VELOCITY)
        await sound.beep(440,200)
        await sound.beep(1661,200)
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, -int(DEGREES_PER_CM*20),0)
        distance = distance - 50  # distance = distance - 50



#runloop.run(main(), main_left(), main_right())
#runloop.run(solution(), solution_right())
runloop.run(other(), other_right())
