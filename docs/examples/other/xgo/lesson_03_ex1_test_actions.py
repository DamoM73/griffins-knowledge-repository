# Exercise 1
#
# Can you test at least 8 actions, one at a time? Record each one in a table
# with the columns Action, What the dog did and Time taken (seconds).
#
def on_button_pressed_a():
    xgo.execution_action(xgo.action_enum.WAVE)
input.on_button_pressed(Button.A, on_button_pressed_a)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
