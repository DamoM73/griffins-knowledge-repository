def on_button_pressed_a():
    xgo.manipulator_clamp(50)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    xgo.manipulator_clamp(200)
input.on_button_pressed(Button.B, on_button_pressed_b)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
xgo.servo_setting_robot_arm(xgo.servo_switch_enum.LOAD)
