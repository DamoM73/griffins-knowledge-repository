# Exercise 3
#
# Can you program a treasure hunt? Hide a "treasure" in the room, then write
# directions from a start mark, such as: face north and walk for 3 seconds,
# face east and walk for 2 seconds. It should:
#
# - turn to face each direction using the compass
# - walk for a set time in that direction
# - show a heart when it reaches the treasure
#
# Swap directions with another group and see whether their dog finds your
# treasure.
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
