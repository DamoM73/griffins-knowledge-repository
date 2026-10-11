# Exercise 2
#
# Can you change the fist angle from 150 to your own angles from Lesson 4?
# How many lines did you have to change? How many would you have changed
# without functions?
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
