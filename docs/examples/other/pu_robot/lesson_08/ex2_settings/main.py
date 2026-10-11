# Exercise 2
#
# Can you add a third variable called rest for the length of the pause, and
# use it in the walk settings program?
#
steps = 4
speed = 5
robotPu.set_walk_speed(robotPu.MoveDirection.FORWARD, steps, speed)
basic.pause(1000)
robotPu.set_walk_speed(robotPu.MoveDirection.BACKWARD, steps, speed)
