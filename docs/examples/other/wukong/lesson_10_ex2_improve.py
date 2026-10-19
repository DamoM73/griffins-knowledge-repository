# Exercise 2
#
# Can you make one design change to improve the grip, then run 5 more
# trials? For example, add rubber bands to the fingertips, change the finger
# angles in make_fist, or curl the fingers in a different order.
#
def make_fist():
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 150)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, 150)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 150)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S5, 150)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S7, 150)

def open_hand():
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, 0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S5, 0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S7, 0)

def on_button_pressed_a():
    make_fist()
    basic.pause(5000)
    open_hand()
input.on_button_pressed(Button.A, on_button_pressed_a)
