from hub import port
import runloop
import motor_pair

async def frightened():
    # move straight for 1440 degrees at a velocity of 1000
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 1440, 0, velocity=1000)

async def normal():
    # move straight for 1440 degrees at a velocity of 250
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 1440, 0, velocity=250)

async def struggle():
    # move straight forward for 1440 degrees at a velocity of 1000 and then repeat backwards
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 1440, 0, velocity=1000)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, -1440, 0, velocity=1000)

async def main():
    # pair motors E and F
    motor_pair.pair(motor_pair.PAIR_1, port.E, port.F)

    await frightened()

    await struggle()

    await normal()

runloop.run(main())