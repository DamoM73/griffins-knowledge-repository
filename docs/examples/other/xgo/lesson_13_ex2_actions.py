# Exercise 2
#
# Can you log the dog doing three built-in actions (such as Wave, Squat and
# Twirl_Roll) and work out which action shakes the micro:bit the most?
#
def on_button_pressed_a():
    xgo.move_xgo(xgo.direction_enum.FORWARD, 50)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    xgo.move_xgo(xgo.direction_enum.FORWARD, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    radio.send_value("x", input.acceleration(Dimension.X))
    radio.send_value("y", input.acceleration(Dimension.Y))
    radio.send_value("z", input.acceleration(Dimension.Z))
    basic.pause(100)
basic.forever(on_forever)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
radio.set_group(42)
