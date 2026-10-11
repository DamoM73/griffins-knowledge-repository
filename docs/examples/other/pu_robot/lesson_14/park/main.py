def on_forever():
    if robotPu.ultrasonic_distance(robotPu.DistanceUnit.CENTIMETERS) > stop_distance:
        robotPu.set_walk_speed(robotPu.MoveDirection.FORWARD, 1, 4)
    else:
        basic.show_icon(IconNames.YES)
basic.forever(on_forever)

stop_distance = 15
