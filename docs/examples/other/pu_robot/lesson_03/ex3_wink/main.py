# Exercise 3
#
# Can you make the robot wink 3 times with its left eye, using a repeat
# loop?
#
for index in range(5):
    robotPu.set_ambience_light(robotPu.LightSelection.ALL, 255, 0, 0)
    basic.pause(500)
    robotPu.set_ambience_light(robotPu.LightSelection.ALL, 0, 0, 255)
    basic.pause(500)
