# Exercise 3
#
# Can you steer the dog by tilting the remote? Hint: send the remote's
# acceleration (mg) x as a number, and turn the dog left or right when it's
# past a threshold.
#
def on_button_pressed_a():
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(0)
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(42)
