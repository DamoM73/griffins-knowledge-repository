# Exercise 2
#
# Can you make a routine that greets us, dances for 5 seconds, stops, then
# kicks?
#
robotPu.execute_action(robotPu.Action.DANCE)
basic.pause(10000)
robotPu.exit_loop()
