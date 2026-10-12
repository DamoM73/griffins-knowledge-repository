# Exercise 2
#
# Can you make the display show a countdown of 3, 2, 1 before the robot
# walks forward? Use the show number block (Basic).
#
robotPu.set_walk_speed_range(2, 2)
basic.show_icon(IconNames.HAPPY)
robotPu.set_walk_speed(robotPu.MoveDirection.FORWARD, 3, 5)
