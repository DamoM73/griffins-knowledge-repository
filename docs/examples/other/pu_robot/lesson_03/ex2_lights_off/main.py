# Exercise 2
#
# Can you make each of the four lights a different colour, then turn them
# off one at a time, one per second?
#
robotPu.set_ambience_light(robotPu.LightSelection.ALL, 255, 0, 0)
basic.pause(1000)
robotPu.set_ambience_light(robotPu.LightSelection.LIGHT1, 0, 0, 255)
