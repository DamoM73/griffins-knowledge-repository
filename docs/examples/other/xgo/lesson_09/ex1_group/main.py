# Exercise 1
#
# Can you change 42 to your pair's radio group in both programs, and test
# that your remote only controls your dog?
#
def on_received_number(receivedNumber):
    if receivedNumber == 1:
        xgo.move_xgo(xgo.direction_enum.FORWARD, 50)
    else:
        xgo.move_xgo(xgo.direction_enum.FORWARD, 0)
radio.on_received_number(on_received_number)

xgo.init_xgo_serial(SerialPin.P14, SerialPin.P13)
radio.set_group(42)
