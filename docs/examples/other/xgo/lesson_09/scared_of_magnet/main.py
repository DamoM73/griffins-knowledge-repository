def on_forever():
    if input.magnetic_force(Dimension.STRENGTH) > 200:
        xgo.move_xgo(xgo.direction_enum.BACKWARD, 30)
    else:
        xgo.move_xgo(xgo.direction_enum.FORWARD, 0)
    basic.pause(200)
basic.forever(on_forever)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
