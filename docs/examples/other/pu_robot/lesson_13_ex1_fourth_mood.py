# Exercise 1
#
# Can you add a fourth mood, surprised, with its own lights, eyes and head
# movement?
#
def on_sound_loud():
    global mood
    mood += 1
    if mood > 3:
        mood = 1
    basic.show_number(mood)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_forever():
    if mood == 1:
        robotPu.set_ambience_light(robotPu.LightSelection.ALL, 255, 200, 0)
        robotPu.set_eyes_state(robotPu.EyeState.ON, robotPu.EyeState.ON)
        robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_PITCH, 110)
    elif mood == 2:
        robotPu.set_ambience_light(robotPu.LightSelection.ALL, 0, 0, 255)
        robotPu.set_left_eye_brightness(10)
        robotPu.set_right_eye_brightness(10)
        robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_PITCH, 70)
    else:
        robotPu.set_ambience_light(robotPu.LightSelection.ALL, 255, 0, 0)
        robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_OFFSET, 70)
        basic.pause(150)
        robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_OFFSET, 110)
        basic.pause(150)
        robotPu.set_servo_angle(robotPu.ServoJoint.HEAD_OFFSET, 90)
    basic.pause(500)
basic.forever(on_forever)

mood = 1
basic.show_number(mood)
