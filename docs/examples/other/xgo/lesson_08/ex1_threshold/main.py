# Exercise 1
#
# How warm does your hand make the micro:bit? Record the temperature before,
# and after 1 and 2 minutes of holding your palm over it. Then choose a
# value for cold that suits your room.
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
