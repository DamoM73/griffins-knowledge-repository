# Exercise 3
#
# Can you change the wave counter so it counts down from 5, and the robot
# greets us when it reaches 0?
#
def on_forever():
    global waves
    if robotPu.ultrasonic_distance(robotPu.DistanceUnit.CENTIMETERS) < 10:
        waves += 1
        basic.show_number(waves)
        basic.pause(1000)
basic.forever(on_forever)

waves = 0
