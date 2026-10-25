# Exercise 1
#
# Does the hand open and close smoothly as you tilt? Why might it jitter?
# Try changing the pause and see whether it helps.
#
def on_forever():
    tilt_angle = input.rotation(Rotation.ROLL) + 90
    finger_angle = Math.constrain(tilt_angle, 0, 150)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, finger_angle)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, finger_angle)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, finger_angle)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S5, finger_angle)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S7, finger_angle)
    basic.pause(50)
basic.forever(on_forever)
