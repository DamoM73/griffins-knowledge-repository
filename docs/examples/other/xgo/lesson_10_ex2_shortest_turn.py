# Exercise 2
#
# The dog always turns left, even when turning right would be quicker. Can
# you make it turn right when the heading is less than 180, and left when
# it's more?
#
def on_forever():
    global heading
    heading = input.compass_heading()
    if heading > 15 and heading < 345:
        xgo.rotate(xgo.rotate_enum.LEFT, 20)
        basic.clear_screen()
    else:
        xgo.rotate(xgo.rotate_enum.LEFT, 0)
        basic.show_string("N")
    basic.pause(100)
basic.forever(on_forever)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
heading = 0
