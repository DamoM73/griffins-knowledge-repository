robotPu.set_controller_radio_group(160)

def on_forever():
    robotPu.send_control_value(robotPu.SendControlType.SPEED, robotPu.read_joystick_value(robotPu.JoystickAxis.SPEED))
    basic.pause(50)
basic.forever(on_forever)
