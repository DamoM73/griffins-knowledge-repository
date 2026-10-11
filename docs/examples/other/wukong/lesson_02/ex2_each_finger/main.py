# Exercise 2
#
# Can you test each finger's servo motor in turn by changing the port,
# pushing the white arm on each time?
#
def on_button_pressed_a():
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 90)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 0)
