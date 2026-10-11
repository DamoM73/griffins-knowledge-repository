robotPu.enable_remote_control_with_group(160)

def on_speed_received(value):
    if value > 0.5:
        robotPu.set_move_direction(robotPu.MoveDirection.FORWARD)
    else:
        robotPu.exit_loop()
robotPu.on_control_value_received(robotPu.ControlValueType.SPEED, on_speed_received)
