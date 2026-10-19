def on_button_pressed_a():
    xgo.manipulator_clamp_x(80)
    basic.pause(1000)
    xgo.manipulator_clamp_z(80)
    basic.pause(1000)
    xgo.manipulator_clamp_x(20)
    xgo.manipulator_clamp_z(20)
input.on_button_pressed(Button.A, on_button_pressed_a)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
xgo.servo_setting_robot_arm(xgo.servo_switch_enum.LOAD)
