from hub import button, light_matrix, port, sound, motion_sensor
import runloop, motor_pair, motor

DEFAULT_VELOCITY = 500
DEGREES_PER_CM = 360/17.5

#0 -> 1
#1 -> -1
    
async def main(): 
    #motor.CLOCKWISE
    
    await motor.run_for_time(port.D, 1000,-DEFAULT_VELOCITY)
    motor.reset_relative_position(port.D, 0)
    await motor.run_to_relative_position(port.D, 70, DEFAULT_VELOCITY)
    sound.beep()
    await motor.run_to_relative_position(port.D, 180, DEFAULT_VELOCITY)

def sign(direction):
    return (0.5-direction)/abs(0.5-direction)

# to have motors run at same time, do not use await
async def run_multiple_for_time(motors, direction, millisecs):
    for m in motors:
        motor.run_for_time(m, millisecs, sign(direction) * DEFAULT_VELOCITY)

async def run_multiple_for_degrees(motors, direction, degrees):
    for m in motors:
        # to have motors run at same time, do not use await
        motor.run_for_degrees(m, degrees, sign(direction) * DEFAULT_VELOCITY)   

async def solution():
    await run_multiple_for_time([port.C, port.D], motor.COUNTERCLOCKWISE, 1000)
    await run_multiple_for_degrees([port.C, port.D], motor.CLOCKWISE, 70)
    sound.beep(440, 200)
    await run_multiple_for_degrees([port.C, port.D], motor.CLOCKWISE, 180)
    await run_multiple_for_degrees([port.C, port.D], motor.COUNTERCLOCKWISE, 180)
    sound.beep(440, 200)
    global DEFAULT_VELOCITY
    DEFAULT_VELOCITY = 150
    await run_multiple_for_degrees([port.C, port.D], motor.CLOCKWISE, 180)
    await run_multiple_for_degrees([port.C, port.D], motor.COUNTERCLOCKWISE, 180)


async def other():
    await run_multiple_for_time([port.C, port.D], motor.COUNTERCLOCKWISE, 1000)
    await run_multiple_for_degrees([port.C, port.D], motor.CLOCKWISE, 70)
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)
    global DEFAULT_VELOCITY
    DEFAULT_VELOCITY = 300
    sound.beep()
    await motor_pair.move_for_degrees(motor_pair.PAIR_1,-180, 0)
    await runloop.sleep_ms(500)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1,180, 0)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1,int(0.77 * 360), 100)
    await runloop.sleep_ms(1000)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1,int(0.4 * 360), 0)
    await motor.run_for_degrees(port.D, 180, DEFAULT_VELOCITY)


runloop.run(main())
