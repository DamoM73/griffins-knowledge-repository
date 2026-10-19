# Exercise 3
#
# Can you add walking backward, and turning left and right? It should:
#
# - walk backward when the joystick is pulled more than halfway back
# - send the joystick's turn value from the remote as well
# - turn left or right when the turn value is past halfway
#
robotPu.enable_remote_control_with_group(160)

def on_speed_received(value):
    if value > 0.5:
        robotPu.set_move_direction(robotPu.MoveDirection.FORWARD)
    else:
        robotPu.exit_loop()
robotPu.on_control_value_received(robotPu.ControlValueType.SPEED, on_speed_received)
