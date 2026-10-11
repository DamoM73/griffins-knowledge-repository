# Exercise 4
#
# Can you make the robot walk forward until something is closer than 15 cm,
# then stop? Hint: start the robot walking with set robot move direction
# before the forever loop.
#
robotPu.set_walk_speed_range(2, 2)

def on_forever():
    pass
basic.forever(on_forever)
