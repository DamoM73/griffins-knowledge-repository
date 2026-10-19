def on_forever():
    basic.show_number(input.temperature())
    basic.pause(1000)
basic.forever(on_forever)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
