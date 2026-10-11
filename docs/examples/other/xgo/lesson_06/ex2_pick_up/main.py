# Exercise 2
#
# Can you program the dog to pick up a scrunched paper ball placed in front
# of it, lift it and drop it?
#
def on_button_pressed_a():
    xgo.Manipulator_clampX(80)
    basic.pause(1000)
    xgo.Manipulator_clampZ(80)
    basic.pause(1000)
    xgo.Manipulator_clampX(20)
    xgo.Manipulator_clampZ(20)
input.on_button_pressed(Button.A, on_button_pressed_a)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
xgo.servo_setting_robotArm(xgo.servo_switch_enum.LOAD)
