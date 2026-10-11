# Exercise 1
#
# How accurate is the ultrasonic sensor? Hold a book at 10, 20 and 30 cm
# from the robot (measure with a ruler) and record what the display shows
# each time.
#
def on_forever():
    basic.show_number(robotPu.ultrasonic_distance(robotPu.DistanceUnit.CENTIMETERS))
basic.forever(on_forever)
