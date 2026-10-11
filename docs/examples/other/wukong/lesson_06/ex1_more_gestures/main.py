# Exercise 1
#
# Can you create functions called point, thumbs_up and peace_sign, and call
# them with A and B together, touching the logo, and shaking the micro:bit?
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
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    open_hand()
input.on_button_pressed(Button.B, on_button_pressed_b)
