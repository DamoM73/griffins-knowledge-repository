# Exercise 3
#
# Can you make the lights show three colours: red when something is closer
# than 10 cm, amber between 10 and 20 cm, and green when it's further away?
# Hint: an if block can have more than one condition. Select the plus sign
# on the if block to add an else if.
#
def on_forever():
    if robotPu.ultrasonic_distance(robotPu.DistanceUnit.CENTIMETERS) < 15:
        robotPu.set_ambience_light(robotPu.LightSelection.ALL, 255, 0, 0)
    else:
        robotPu.set_ambience_light(robotPu.LightSelection.ALL, 0, 255, 0)
basic.forever(on_forever)
