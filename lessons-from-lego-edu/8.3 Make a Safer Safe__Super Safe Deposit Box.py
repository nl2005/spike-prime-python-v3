from hub import sound, port, light_matrix, button
import app
import runloop
import time
import motor

async def main():
    await sound.beep(262, 200)
    await sound.beep(523, 200)

    #this locks the safe
    await motor.run_for_time(port.C, 1000, -500)
    await motor.run_to_absolute_position(port.B, 0, 500, stop=motor.COAST)
    motor.reset_relative_position(port.B, 0)
    await motor.run_to_absolute_position(port.E, 0, 500)
    light_matrix.show_image(light_matrix.IMAGE_NO)

    #this unlocks the safe
    await unlock()

async def unlock():
    start_time = time.ticks_ms()
    while not button.pressed(button.LEFT) and motor.relative_position(port.B) < 180:
        await sound.beep(262, 200)
        await motor.run_for_degrees(port.E, 15, 500)
        await runloop.sleep_ms(800)
        if time.ticks_diff(time.ticks_ms(), start_time) > 5000:
            await app.sound.play('Bonk')
            return
        light_matrix.show_image(light_matrix.IMAGE_NO)

    light_matrix.show_image(light_matrix.IMAGE_YES)
    await motor.run_to_absolute_position(port.E, 0, 500)
    await motor.run_for_time(port.C, 1000, 500)
    await app.sound.play('Wand')

runloop.run(main())