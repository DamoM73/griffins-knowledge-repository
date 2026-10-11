# Exercise 1
#
# What happens if we take out the set XGO block and press A? Why do you
# think this happens?
#
def on_button_pressed_a():
    xgo.execution_action(xgo.action_enum.SIT_DOWN)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(xgo.get_electric_quantity())
input.on_button_pressed(Button.B, on_button_pressed_b)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
basic.show_icon(IconNames.HAPPY)
