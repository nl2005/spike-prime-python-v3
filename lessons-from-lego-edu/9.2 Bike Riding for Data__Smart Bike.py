from hub import port, light_matrix, button
import runloop
import motor_pair

async def ride(bike_velocity):
    #defines the ride function to write the velocity on the hub and move the bike farward
    await light_matrix.write(str(bike_velocity))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 720, 0, velocity=bike_velocity)

async def main():
    bike_velocity = 250
    #pair motors
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.E)

    while True:
        #if the left button is pressed the velocity is reduced by 50
        if button.pressed(button.LEFT):
            bike_velocity -= 50
            await ride(bike_velocity)
            await runloop.sleep_ms(2000)

        #if the right button is pressed the velocity is increaded by 50
        if button.pressed(button.RIGHT):
            bike_velocity += 50
            await ride(bike_velocity)
            await runloop.sleep_ms(2000)

runloop.run(main())