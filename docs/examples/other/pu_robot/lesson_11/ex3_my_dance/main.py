# Exercise 3
#
# Can you make a dance with at least three different moves and changing
# light colours, timed to a melody of your choice?
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
