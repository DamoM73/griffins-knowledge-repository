# Exercise 1
#
# What range of values does body roll give? Change the example to show body
# roll, tilt the robot gently from side to side, and record the lowest and
# highest numbers.
#
def on_forever():
    basic.show_number(robotPu.body_pitch())
    basic.pause(500)
basic.forever(on_forever)
