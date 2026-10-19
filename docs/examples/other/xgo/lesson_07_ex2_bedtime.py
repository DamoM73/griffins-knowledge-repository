# Exercise 2
#
# Can you make the dog lie down (Go_prone) when it's dark, and stand up when
# it's bright?
#
def on_forever():
    if input.light_level() > 100:
        xgo.move_xgo(xgo.direction_enum.FORWARD, 30)
    else:
        xgo.move_xgo(xgo.direction_enum.FORWARD, 0)
    basic.pause(200)
basic.forever(on_forever)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
