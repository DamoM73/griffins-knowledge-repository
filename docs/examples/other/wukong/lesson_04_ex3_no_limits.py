# Exercise 3
#
# What happens if we take the if lines out and keep pressing B? Why do you
# think the program needs them?
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
