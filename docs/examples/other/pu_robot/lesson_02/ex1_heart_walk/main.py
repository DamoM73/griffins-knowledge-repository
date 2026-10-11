# Exercise 1
#
# Can you make the robot show a heart, walk forward 5 steps, then show a
# happy face?
#
robotPu.set_walk_speed_range(2, 2)
basic.show_icon(IconNames.HAPPY)
robotPu.set_walk_speed(robotPu.MoveDirection.FORWARD, 3, 5)
