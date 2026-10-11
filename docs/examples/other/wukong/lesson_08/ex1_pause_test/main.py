# Exercise 1
#
# How does the pause change the speed? Change the pause to 5, 50 and 100 ms,
# time how long the finger takes to curl each time with a stopwatch, and
# record the results in a table.
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
