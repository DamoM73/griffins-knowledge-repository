# Exercise 2
#
# Can you add a program for pressing A and B together that makes the dog
# stand back up? Use the Stand action.
#
def on_button_pressed_a():
    xgo.execution_action(xgo.action_enum.SIT_DOWN)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(xgo.get_electric_quantity())
input.on_button_pressed(Button.B, on_button_pressed_b)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
basic.show_icon(IconNames.HAPPY)
