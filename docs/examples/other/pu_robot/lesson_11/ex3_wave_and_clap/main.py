# Exercise 3
#
# Can you make the robot greet you when you wave your hand, and jump when
# you clap?
#
def on_sound_loud():
    robotPu.execute_action(robotPu.Action.JUMP)
input.on_sound(DetectedSound.LOUD, on_sound_loud)
