# Exercise 4
#
# How accurate is the music tempo? Play three songs whose BPM you can look
# up online, and compare the robot's tempo with the real one.
#
def on_forever():
    basic.show_number(robotPu.music_tempo())
    basic.pause(1000)
basic.forever(on_forever)
