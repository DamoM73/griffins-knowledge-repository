def on_button_pressed_b():
    xgo.rotate(xgo.rotate_enum.LEFT, 50)
    basic.pause(2000)
    xgo.rotate(xgo.rotate_enum.LEFT, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
