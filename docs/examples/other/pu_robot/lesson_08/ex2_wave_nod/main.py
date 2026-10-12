# Exercise 2
#
# Can you make the robot nod its head when you wave your hand in front of
# it?
#
def on_forever():
    if robotPu.ultrasonic_distance(robotPu.DistanceUnit.CENTIMETERS) < 10:
        robotPu.execute_action(robotPu.Action.GREET)
        basic.pause(1000)
basic.forever(on_forever)
