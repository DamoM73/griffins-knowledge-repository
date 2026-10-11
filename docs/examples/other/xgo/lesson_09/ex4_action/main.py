# Exercise 4
#
# Can you add a gesture on the remote, such as shaking it, that makes the
# dog do a built-in action?
#
def on_button_pressed_a():
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(42)
