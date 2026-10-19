# Exercise 2
#
# Is the hand really random? Shake it 30 times and tally how many times it
# picks each gesture. Are the three totals close?
#
def rock():
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 150)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, 150)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 150)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S5, 150)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S7, 150)

def paper():
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, 0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S5, 0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S7, 0)

def scissors():
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 150)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S1, 0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S3, 0)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S5, 150)
    wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S7, 150)

def on_gesture_shake():
    choice = randint(1, 3)
    if choice == 1:
        rock()
    elif choice == 2:
        paper()
    else:
        scissors()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
