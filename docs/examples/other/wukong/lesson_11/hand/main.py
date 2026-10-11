def make_fist():
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 150)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, 150)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 150)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S5, 150)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S7, 150)

def open_hand():
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, 0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S5, 0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S7, 0)

def on_received_number(receivedNumber):
    if receivedNumber == 1:
        make_fist()
    else:
        open_hand()
radio.on_received_number(on_received_number)

radio.set_group(42)
