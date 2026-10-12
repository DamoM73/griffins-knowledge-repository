# Exercise 4
#
# What happens if we take the pauses out of the smooth move example? Why do
# you think this happens?
#
robotPu.smooth_set_servo_angle(robotPu.ServoJoint.HEAD_OFFSET, 60, 2)
basic.pause(2000)
robotPu.smooth_set_servo_angle(robotPu.ServoJoint.HEAD_OFFSET, 120, 2)
basic.pause(2000)
robotPu.smooth_set_servo_angle(robotPu.ServoJoint.HEAD_OFFSET, 90, 2)
