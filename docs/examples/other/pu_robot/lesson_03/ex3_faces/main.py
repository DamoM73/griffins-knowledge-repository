# Exercise 3
#
# Can you make a forever loop that shows a happy face, then a sad face, then
# a surprised face, with half a second between each one?
#
def on_forever():
    basic.show_icon(IconNames.HAPPY)
    basic.pause(1000)
    basic.show_icon(IconNames.HEART)
    basic.pause(1000)
basic.forever(on_forever)
