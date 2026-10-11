# Exercise 3
#
# What does clmap stable is stable do? Set it to stable, then change the
# body height while the gripper holds the ball. Repeat with unstable and
# compare what happens to the gripper's position.
#
def on_button_pressed_a():
    xgo.Manipulator_clamp(50)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    xgo.Manipulator_clamp(200)
input.on_button_pressed(Button.B, on_button_pressed_b)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
xgo.servo_setting_robotArm(xgo.servo_switch_enum.LOAD)
