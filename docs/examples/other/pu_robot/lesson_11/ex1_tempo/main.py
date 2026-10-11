# Exercise 1
#
# What happens to the dance if we change the tempo to 60, then to 180? Why
# does one change make the moves faster or slower?
#
def on_forever():
    if robotPu.ultrasonic_distance(robotPu.DistanceUnit.CENTIMETERS) < 10:
        music.play(music.builtin_playable_melody(Melodies.ENTERTAINER), music.PlaybackMode.IN_BACKGROUND)
        for index in range(4):
            robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_OFFSET, 60)
            basic.pause(music.beat(BeatFraction.WHOLE))
            robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_OFFSET, 120)
            basic.pause(music.beat(BeatFraction.WHOLE))
        robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_OFFSET, 90)
basic.forever(on_forever)

music.set_tempo(120)
