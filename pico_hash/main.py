from hashmoves import HashMoves
from hashfacialexp import HashFacialExp
from machine import I2C, Pin
from time import sleep


sda = Pin(0)
scl = Pin(1)
id = 0
i2c = I2C(0, sda=sda, scl=scl)

hf=HashFacialExp()  
hm=HashMoves()

hf.initialize(i2c)
hm.initialize(i2c)
hf.default_face()
sleep(2)
hf.happy_face()
hf.sad_face()
hf.eyeclose_face()
hf.blink(5)
hf.sleep_face(5)
hf.wink_face()
hf.hardcry_face(3)
hf.love_face()
hf.angry_face()
hf.shock_face()
hm.say_hi(2000,2)
hm.hands_up(2000,1)
hm.hands_down(2000,1)
hm.move_forward(500,5)
hm.move_backward(500,5)
hm.turn_left(500,5)
hm.turn_right(500,5)
hm.side_move_right(500,5)
hm.side_move_left(500,5)
hm.flying_move(1000,3)
hm.leg_shake(1000,3)
hm.hand_straight_shake(1000,3)
hm.leg_head_shake(1000,3)
hm.jump(1000,3)
hm.right_slide_wave(2000,3)
hm.left_slide_wave(2000,3)
hm.right_hand_balance(2000,3)
hm.left_hand_balance(2000,3)
hm.side_shake(1000,2)



