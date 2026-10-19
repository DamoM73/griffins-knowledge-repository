def on_logo_pressed():
    xgo.execution_action(xgo.action_enum.STRETCH_ONESELF)
    xgo.execution_action(xgo.action_enum.HANDSHAKE)
    xgo.init_action()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
