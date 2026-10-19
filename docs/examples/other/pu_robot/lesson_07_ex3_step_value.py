# Exercise 3
#
# What difference does the step value make in smooth move? Try steps of 1, 5
# and 20, and describe how each one looks.
#
robotPu.smooth_set_servo_angle(robotPu.ServoJoint.HEAD_OFFSET, 60, 2)
basic.pause(2000)
robotPu.smooth_set_servo_angle(robotPu.ServoJoint.HEAD_OFFSET, 120, 2)
basic.pause(2000)
robotPu.smooth_set_servo_angle(robotPu.ServoJoint.HEAD_OFFSET, 90, 2)
