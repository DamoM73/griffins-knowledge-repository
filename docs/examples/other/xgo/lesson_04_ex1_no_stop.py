# Exercise 1
#
# What happens if we take out the last move line (speed 0)? Predict first,
# then test it, ready to switch the dog off.
#
def on_button_pressed_a():
    xgo.move_xgo(xgo.direction_enum.FORWARD, 50)
    basic.pause(3000)
    xgo.move_xgo(xgo.direction_enum.FORWARD, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
