def on_forever():
    basic.show_number(robotPu.body_pitch())
    basic.pause(500)
basic.forever(on_forever)
