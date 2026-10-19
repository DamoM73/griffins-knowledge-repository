# Exercise 1
#
# What angle makes each finger fully curled? It should:
#
# 1. press A until the thumb is fully curled, stopping as soon as it stops
#    moving or the servo motor buzzes
# 2. record the angle in a table with the columns Finger, Port and Fully
#    curled angle
# 3. change the port and repeat for each finger
#
# We use these angles instead of 180 in all the later lessons.
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
