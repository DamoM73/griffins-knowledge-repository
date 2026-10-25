# Exercise 3
#
# Can you give each finger a different range, so the fingers curl one after
# another as you tilt? For example, the thumb curls over the first part of
# the tilt and the little finger over the last part.
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
