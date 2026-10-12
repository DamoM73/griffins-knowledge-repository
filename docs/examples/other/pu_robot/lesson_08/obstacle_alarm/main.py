def on_forever():
    if robotPu.ultrasonic_distance(robotPu.DistanceUnit.CENTIMETERS) < 15:
        robotPu.set_ambience_light(robotPu.LightSelection.ALL, 255, 0, 0)
    else:
        robotPu.set_ambience_light(robotPu.LightSelection.ALL, 0, 255, 0)
basic.forever(on_forever)
