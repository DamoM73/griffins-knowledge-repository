# Exercise 1
#
# Can you change the program so the dog turns to face east (90 degrees)
# instead? Hint: east is in the middle of the range, so we don't need to
# worry about the jump from 359 to 0.
#
def on_forever():
    global heading
    heading = input.compass_heading()
    if heading > 15 and heading < 345:
        xgo.rotate(xgo.rotate_enum.LEFT, 20)
        basic.clear_screen()
    else:
        xgo.rotate(xgo.rotate_enum.LEFT, 0)
        basic.show_string("N")
    basic.pause(100)
basic.forever(on_forever)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
heading = 0
