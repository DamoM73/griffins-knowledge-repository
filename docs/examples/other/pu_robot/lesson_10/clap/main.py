def on_sound_loud():
    robotPu.execute_action(robotPu.Action.JUMP)
input.on_sound(DetectedSound.LOUD, on_sound_loud)
