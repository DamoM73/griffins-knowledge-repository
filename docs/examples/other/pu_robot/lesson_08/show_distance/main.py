def on_forever():
    basic.show_number(robotPu.ultrasonic_distance(robotPu.DistanceUnit.CENTIMETERS))
basic.forever(on_forever)
