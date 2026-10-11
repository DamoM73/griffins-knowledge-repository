# Exercise 2
#
# Can you make the robot shake its head "no" by moving the head offset
# joint?
#
robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_PITCH, 70)
basic.pause(500)
robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_PITCH, 110)
basic.pause(500)
robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_PITCH, 90)
