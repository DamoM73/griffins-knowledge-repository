def on_button_pressed_a():
    xgo.translational_step_continue(xgo.translation_direction_enum.FORWARD, 15, 3)
input.on_button_pressed(Button.A, on_button_pressed_a)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
