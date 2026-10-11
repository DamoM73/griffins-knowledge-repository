# Exercise 3
#
# Can you add a second threshold, hot, so the dog pants (shows an icon of
# your choice and lowers its body) when it's too warm?
#
def on_forever():
    if input.temperature() < cold:
        for index in range(5):
            xgo.rotate_angle_reel(xgo.body_direction_xyz_enum.Y, 5)
            basic.pause(100)
            xgo.rotate_angle_reel(xgo.body_direction_xyz_enum.Y, -5)
            basic.pause(100)
        xgo.rotate_angle_reel(xgo.body_direction_xyz_enum.Y, 0)
    basic.pause(1000)
basic.forever(on_forever)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
cold = 22
