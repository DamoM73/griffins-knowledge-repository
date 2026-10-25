# Exercise 1
#
# Does the hand open and close smoothly as you tilt? Why might it jitter?
# Try changing the pause and see whether it helps.
#
def on_forever():
    angle = input.rotation(Rotation.ROLL) + 90
    angle = Math.constrain(angle, 0, 150)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, angle)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, angle)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, angle)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S5, angle)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S7, angle)
    basic.pause(50)
basic.forever(on_forever)
