# Exercise 2
#
# Can you record 3 different poses and play them one after another as an
# animation? Use pose 1, pose 2 and pose 3, with a pause between each.
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
