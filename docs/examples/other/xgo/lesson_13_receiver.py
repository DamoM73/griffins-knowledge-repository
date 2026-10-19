def on_received_value(name, value):
    serial.write_value(name, value)
radio.on_received_value(on_received_value)

radio.set_group(42)
