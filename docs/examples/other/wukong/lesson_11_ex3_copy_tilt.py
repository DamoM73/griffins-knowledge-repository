# Exercise 3
#
# Can you make the hand copy how far the remote is tilted? It should:
#
# - send the remote's acceleration (mg) x as a number, about 10 times a
#   second, in a forever loop
# - map the number to an angle on the hand, as in Lesson 9
# - set all 5 fingers to that angle
#
def on_button_pressed_a():
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(2)
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(42)
