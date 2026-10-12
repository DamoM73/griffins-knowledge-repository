# Exercise 1
#
# Can you make a traffic light sequence on all four lights? It should:
#
# 1. show green for 3 seconds
# 2. show amber (255, 120, 0) for 1 second
# 3. show red for 3 seconds
#
robotPu.set_ambience_light(robotPu.LightSelection.ALL, 255, 0, 0)
basic.pause(1000)
robotPu.set_ambience_light(robotPu.LightSelection.LIGHT1, 0, 0, 255)
