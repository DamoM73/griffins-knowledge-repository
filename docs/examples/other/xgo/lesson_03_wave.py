def on_button_pressed_a():
    xgo.execution_action(xgo.action_enum.WAVE)
input.on_button_pressed(Button.A, on_button_pressed_a)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
