music.set_tempo(120)
for index in range(8):
    robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_PITCH, 70)
    basic.pause(music.beat(BeatFraction.HALF))
    robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_PITCH, 110)
    basic.pause(music.beat(BeatFraction.HALF))
robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_PITCH, 90)
