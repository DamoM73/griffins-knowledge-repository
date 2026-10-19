# Exercise 2
#
# Can you make the hand count the other way? It should start as a fist and
# straighten one finger per second, counting 1 to 5 on the display.
#
def on_button_pressed_a():
    basic.show_number(1)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 150)
    basic.pause(1000)
    basic.show_number(2)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, 150)
    basic.pause(1000)
    basic.show_number(3)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 150)
    basic.pause(1000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, 0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 0)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)
