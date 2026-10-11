# Exercise 1
#
# How does the speed setting change how far the robot walks? It should:
#
# 1. walk forward 5 steps at speed 2, then measure the distance from a tape
#    start line in centimetres
# 2. repeat at speeds 5 and 8, running each speed 3 times
# 3. record the results in a table
#
# What's the relationship between speed and distance travelled?
#
robotPu.set_walk_speed(robotPu.MoveDirection.FORWARD, 5, 2)
