from hub import port, sound, light_matrix, button
import runloop
import motor

def pressed():
    return button.pressed(button.LEFT)>0

async def main():
    await sound.beep(262, 200)
    await sound.beep(523, 200)

    #this locks the safe
    motor.stop(port.B)
    motor.reset_relative_position(port.B, 0)
    await motor.run_to_absolute_position(port.C, 270, 500)
    light_matrix.show_image(light_matrix.IMAGE_NO)

    #this unlocks the safe
    while True:
        print('Open Me')
        if motor.relative_position(port.B) > 180:
            await runloop.until(pressed)
            await sound.beep(523, 200)
            await motor.run_for_time(port.C, 1000, 500)
            light_matrix.show_image(light_matrix.IMAGE_YES)
            await runloop.sleep_ms(5000)
            break
        else:
            print('Still Locked!')
            await runloop.sleep_ms(1000)

    print('You may enter!')
runloop.run(main())