# Exercise 4
#
# Can you change the walk speed range so the robot walks faster forward than
# backward? Test it with set robot move direction. The forward level goes
# from 0 to 4, and the backward level from 0 to 3.
#
robotPu.set_walk_speed_range(2, 2)
robotPu.set_move_direction(robotPu.MoveDirection.FORWARD)
basic.pause(3000)
robotPu.exit_loop()
