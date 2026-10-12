# Exercise 1
#
# Can you make the robot nod "yes" 3 times using a repeat loop?
#
robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_PITCH, 70)
basic.pause(500)
robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_PITCH, 110)
basic.pause(500)
robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_PITCH, 90)
