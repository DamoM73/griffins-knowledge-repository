# Exercise 2
#
# How does step size change how far the dog walks? It should:
#
# 1. walk forward for 3 seconds with step sizes of 5, 15 and 25 mm
# 2. measure the distance from a tape start line each time
# 3. run each step size 3 times and record the results in a table
#
def on_button_pressed_a():
    xgo.translational_step_continue(xgo.translation_direction_enum.FORWARD, 15, 3)
input.on_button_pressed(Button.A, on_button_pressed_a)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
