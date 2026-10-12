def on_forever():
    global distance
    distance = robotPu.ultrasonic_distance(robotPu.DistanceUnit.CENTIMETERS)
    if distance > 30:
        robotPu.set_ambience_light(robotPu.LightSelection.ALL, 0, 255, 0)
        robotPu.set_walk_speed(robotPu.MoveDirection.FORWARD, 1, 5)
    elif distance > 10:
        robotPu.set_ambience_light(robotPu.LightSelection.ALL, 255, 120, 0)
        robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_OFFSET, 70)
        basic.pause(300)
        robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_OFFSET, 110)
        basic.pause(300)
        robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_OFFSET, 90)
    else:
        robotPu.set_ambience_light(robotPu.LightSelection.ALL, 255, 0, 0)
        robotPu.set_walk_speed(robotPu.MoveDirection.BACKWARD, 2, 5)
basic.forever(on_forever)

distance = 0
