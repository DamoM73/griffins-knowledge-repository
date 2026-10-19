# Exercise 2
#
# Can you change the program so each button press moves the finger by 5
# degrees instead of 10?
#
def on_button_pressed_a():
    global angle
    if angle < 180:
        angle += 10
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, angle)
    basic.show_number(angle)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global angle
    if angle > 0:
        angle -= 10
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, angle)
    basic.show_number(angle)
input.on_button_pressed(Button.B, on_button_pressed_b)

angle = 0
wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, angle)
