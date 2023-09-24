from hub import button, light_matrix, port, sound, motion_sensor
import runloop, motor_pair

DEFAULT_VELOCITY = 500
DEGREES_PER_CM = 360/17.5

async def forward():
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 20 * 360, 0)

async def square():
    for i in range(4):
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(1.5 * 360), 0)
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(0.365 * 360), 100)

async def triangle():
    for i in range(3):
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(1.5 * 360), 0)
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(0.486 * 360), 100)

async def circle():
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, int(3 * 360), 60)
    
async def main(): 
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D) 
    
    await forward()
    sound.beep()
    await square()
    sound.beep()
    await triangle()
    sound.beep()
    await circle()
    sound.beep()


runloop.run(main())
