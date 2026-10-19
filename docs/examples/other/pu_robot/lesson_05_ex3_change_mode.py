# Exercise 3
#
# What happens if we use set mode to start a new mode while another mode is
# still running? Why do you think this happens?
#
robotPu.execute_action(robotPu.Action.DANCE)
basic.pause(3000)
robotPu.execute_action(robotPu.Action.GREET)
