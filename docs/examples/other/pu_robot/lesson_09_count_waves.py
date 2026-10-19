def on_forever():
    global waves
    if robotPu.ultrasonic_distance(robotPu.DistanceUnit.CENTIMETERS) < 10:
        waves += 1
        basic.show_number(waves)
        basic.pause(1000)
basic.forever(on_forever)

waves = 0
