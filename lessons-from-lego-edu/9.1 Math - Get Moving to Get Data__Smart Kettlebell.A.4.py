from hub import port
import runloop
import distance_sensor
import force_sensor

async def main():
    #read the distance from the sensor
    while True:
        if force_sensor.pressed(port.B):
            dist_mm = distance_sensor.distance(port.F)
            print('mm:', dist_mm)
            await runloop.sleep_ms(1000)

runloop.run(main())