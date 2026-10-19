def on_forever():
    global visitors
    if robotPu.ultrasonic_distance(robotPu.DistanceUnit.CENTIMETERS) < 20:
        robotPu.set_ambience_light(robotPu.LightSelection.ALL, 0, 0, 255)
        robotPu.execute_action(robotPu.Action.GREET)
        visitors += 1
        basic.show_number(visitors)
        basic.pause(3000)
    else:
        robotPu.set_ambience_light(robotPu.LightSelection.ALL, 0, 255, 0)
basic.forever(on_forever)

visitors = 0
