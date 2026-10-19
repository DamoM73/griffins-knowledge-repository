# Exercise 1
#
# Can you test rotation around the X, Y and Z axes? Sketch the dog from
# above and from the side, and label which way each axis tilts it.
#
def on_button_pressed_a():
    xgo.rotate_angle_reel(xgo.body_direction_xyz_enum.X, 15)
    basic.pause(1000)
    xgo.rotate_angle_reel(xgo.body_direction_xyz_enum.X, -15)
    basic.pause(1000)
    xgo.rotate_angle_reel(xgo.body_direction_xyz_enum.X, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
