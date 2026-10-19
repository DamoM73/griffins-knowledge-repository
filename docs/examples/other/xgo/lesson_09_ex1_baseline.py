# Exercise 1
#
# What's the reading with no magnet near, and how much does it change while
# the dog walks? Record both, then choose a better threshold. This starting
# reading is called a baseline.
#
def on_forever():
    if input.magnetic_force(Dimension.STRENGTH) > 200:
        xgo.move_xgo(xgo.direction_enum.BACKWARD, 30)
    else:
        xgo.move_xgo(xgo.direction_enum.FORWARD, 0)
    basic.pause(200)
basic.forever(on_forever)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
