def on_forever():
    basic.show_icon(IconNames.HAPPY)
    basic.pause(1000)
    basic.show_icon(IconNames.HEART)
    basic.pause(1000)
basic.forever(on_forever)
