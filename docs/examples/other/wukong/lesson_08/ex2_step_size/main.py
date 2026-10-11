# Exercise 2
#
# What's the relationship between the pause, the step size and the total
# time? Work out how many steps the loop takes to reach 150, then predict
# the total time before testing.
#
def on_button_pressed_a():
    angle = 0
    while angle <= 150:
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, angle)
        angle += 5
        basic.pause(20)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)
