# Exercise 2
#
# Can you make the lights turn red when the robot is tilted too far forwards
# or backwards, and green when it's level? Use your numbers from the first
# example to choose how far is too far.
#
def on_forever():
    basic.show_number(robotPu.body_pitch())
    basic.pause(500)
basic.forever(on_forever)
