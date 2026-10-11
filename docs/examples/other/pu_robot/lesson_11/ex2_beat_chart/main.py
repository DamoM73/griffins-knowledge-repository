# Exercise 2
#
# Can you draw a beat chart for 8 beats of moves (nod, shake, wink and so
# on), then program it?
#
music.set_tempo(120)
for index in range(8):
    robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_PITCH, 70)
    basic.pause(music.beat(BeatFraction.HALF))
    robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_PITCH, 110)
    basic.pause(music.beat(BeatFraction.HALF))
robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_PITCH, 90)
