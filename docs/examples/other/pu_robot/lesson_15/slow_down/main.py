def on_forever():
    global distance
    distance = robotPu.ultrasonic_distance(robotPu.DistanceUnit.CENTIMETERS)
    if distance > slow_distance:
        robotPu.set_walk_speed(robotPu.MoveDirection.FORWARD, 1, 6)
    elif distance > stop_distance:
        robotPu.set_walk_speed(robotPu.MoveDirection.FORWARD, 1, 2)
    else:
        basic.show_icon(IconNames.YES)
basic.forever(on_forever)

distance = 0
slow_distance = 30
stop_distance = 8
