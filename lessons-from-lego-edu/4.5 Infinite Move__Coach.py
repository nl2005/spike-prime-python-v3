from hub import port, motion_sensor
import runloop
import motor
import force_sensor


def is_pressed():
    return motion_sensor.tap_count() > 0

def is_pressed_too_much():
    print(motion_sensor.tap_count())
    return motion_sensor.tap_count() > 1

def should_run():
    motion_sensor.tap_count() % 2 == 1

# def stop_run():
#     motion_sensor.tap_count() % 2 == 0

async def main():
    motion_sensor.reset_tap_count()

    while not should_run():
        # when the force sensor is pressed, start coach
       
        # print(motion_sensor.tap_count())
        
        await runloop.until(should_run)

        # Run at 300 velocity for 1/4 second
        await motor.run_for_time(port.B, 250, 300)
        await motor.run_for_time(port.A, 250, 300)
        await motor.run_for_time(port.B, 250, -300)
        await motor.run_for_time(port.A, 250, -300)

        # if is_pressed_too_much():
        #     break
    '''
    if should_run():
        await motor.run_for_time(port.B, 250, 300)
        await motor.run_for_time(port.A, 250, 300)
        await motor.run_for_time(port.B, 250, -300)
        await motor.run_for_time(port.A, 250, -300)
    else 
    '''


runloop.run(main())