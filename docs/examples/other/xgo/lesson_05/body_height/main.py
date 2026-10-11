def on_button_pressed_a():
    xgo.body_height(20)
    basic.pause(1000)
    xgo.body_height(100)
    basic.pause(1000)
    xgo.body_height(50)
input.on_button_pressed(Button.A, on_button_pressed_a)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
