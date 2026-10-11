# Exercise 3
#
# Can you use the micro:bit's compass heading to make the dog turn until it
# faces north? Hint: north is a heading close to 0 or 360 degrees.
#
def on_forever():
    basic.show_number(input.compass_heading())
basic.forever(on_forever)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
