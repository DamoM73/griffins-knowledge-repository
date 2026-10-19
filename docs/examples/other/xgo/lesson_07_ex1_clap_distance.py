# Exercise 1
#
# How loud does a clap need to be? Try clapping from 1, 2 and 3 metres away,
# and record whether the dog reacts each time.
#
def on_sound_loud():
    xgo.execution_action(xgo.action_enum.SIT_DOWN)
    xgo.execution_action(xgo.action_enum.STAND)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
