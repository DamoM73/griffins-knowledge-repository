# Exercise 1
#
# Can you teach the dog a pose that uses two legs? Unload both front legs,
# move them, then record the pose.
#
def on_button_pressed_a():
    xgo.servo_setting(xgo.body_parts_enum.LEFT_FRONT, xgo.servo_switch_enum.UNLOAD)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    xgo.get_posestate(xgo.pose_enum.POSE1)
    xgo.servo_setting(xgo.body_parts_enum.LEFT_FRONT, xgo.servo_switch_enum.LOAD)
    xgo.init_action()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    xgo.set_posestate(xgo.pose_enum.POSE1)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
