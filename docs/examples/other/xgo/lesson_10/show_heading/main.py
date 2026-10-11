def on_forever():
    basic.show_number(input.compass_heading())
    basic.pause(500)
basic.forever(on_forever)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
