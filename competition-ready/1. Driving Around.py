from hub import button, light_matrix, port, sound, motion_sensor
import runloop, motor_pair

DEFAULT_VELOCITY = 360
DEGREES_PER_CM = 360/17.5

def setup():
    
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.E)
    global DEFAULT_VELOCITY
    DEFAULT_VELOCITY  = 10 * 50 
    global DEGREES_PER_CM
    DEGREES_PER_CM = 360 / 17.5

async def main(): 
    setup()  
    await runloop.sleep_ms(1000)
    motion_sensor.reset_yaw(0)
    motor_pair.move(motor_pair.PAIR_1, 100, velocity=DEFAULT_VELOCITY)
    await runloop.until(lambda: motion_sensor.tilt_angles()[0] > 89)
    motor_pair.stop(motor_pair.PAIR_1)

    await runloop.sleep_ms(1000)

    #await drive_square_loop()
    await drive_square_yaw()


async def main_left():
    #while True:
        await runloop.until(lambda: button.pressed(button.LEFT)>0)
        sound.beep(440)
        await runloop.sleep_ms(1000)
    #await motor_pair.move_for_degrees(motor_pair.PAIR_1,int(DEGREES_PER_CM * 20),0, velocity=DEFAULT_VELOCITY)
    #await motor_pair.move_for_degrees(motor_pair.PAIR_1,-int(DEGREES_PER_CM * 20),0, velocity=DEFAULT_VELOCITY)

async def main_right():
    #while True:
        await runloop.until(lambda: button.pressed(button.RIGHT)>0)
        sound.beep(1440)
        await runloop.sleep_ms(1000)
    #    motor_pair.move_for_degrees(motor_pair.PAIR_1, 360*20,-40, velocity=DEFAULT_VELOCITY)


async def drive_square_loop():
    await runloop.sleep_ms(1000)
    for i in range(4):
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(DEGREES_PER_CM*10), 0, velocity=300 )
        await runloop.sleep_ms(500)
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, 180 ,100)
        motor_pair.stop(motor_pair.PAIR_1)

async def drive_square_yaw():
    await runloop.sleep_ms(1000)
    for i in range(4):
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(DEGREES_PER_CM*10), 0, velocity=300 )
        await runloop.sleep_ms(500)
        motion_sensor.reset_yaw(0)
        await runloop.sleep_ms(500)
        motor_pair.move(motor_pair.PAIR_1, 100, velocity=DEFAULT_VELOCITY)
        await runloop.until(lambda: motion_sensor.tilt_angles()[0] > 89)
        motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main_left(),main_right())
