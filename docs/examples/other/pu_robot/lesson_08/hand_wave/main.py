def on_forever():
    if robotPu.ultrasonic_distance(robotPu.DistanceUnit.CENTIMETERS) < 10:
        robotPu.execute_action(robotPu.Action.GREET)
        basic.pause(1000)
basic.forever(on_forever)
