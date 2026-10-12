# Exercise 4
#
# Can you use the remote's B1 to B4 buttons to start modes such as dance and
# kick? Hint: on the remote, use initialize controller buttons and B1
# pressed (robot PU > Controller), and send a button value. On the robot,
# use on button value received.
#
robotPu.set_controller_radio_group(160)

def on_forever():
    robotPu.send_control_value(robotPu.SendControlType.SPEED, robotPu.read_joystick_value(robotPu.JoystickAxis.SPEED))
    basic.pause(50)
basic.forever(on_forever)
