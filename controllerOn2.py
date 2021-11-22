#kotelezo resz
from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor, UltrasonicSensor
from ev3dev2.led import Leds

#sajat cuccok

def main():
    speed = 70
    motor_l = LargeMotor(OUTPUT_A)
    motor_r = LargeMotor(OUTPUT_B)
    motors = MoveTank(OUTPUT_A, OUTPUT_B)

    sensor_us = UltrasonicSensor(INPUT_1)

    while sensor_us.distance_centimeters > 5:
        while sensor_us.distance_centimeters > 20:
            motors.on(SpeedPercent(speed), SpeedPercent(speed))
        motors.on_for_seconds(speed,-speed,2)

if __name__=="__main__":
    main()