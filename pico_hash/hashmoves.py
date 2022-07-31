from pca9685 import PCA9685
from machine import I2C, Pin
from servo import Servos
from time import sleep

class HashMoves:

    def initialize(self,i2c):
        self.pca = PCA9685(i2c=i2c)
        self.servo = Servos(i2c=i2c)
        self.servo.initial_position()
        
    def say_hi(self,time,count):
        pwm_array1 = [160, 60, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array1)
        for x in range(3):
            pwm_array2 = [160, 30, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array3 = [160, 60, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            self.servo.moveservo(time/2, pwm_array2)
            self.servo.moveservo(time/2, pwm_array3)
        pwm_array4 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array4)

    def hands_up(self,time,count):
        pwm_array1 = [180, 0, 90, 90, 0, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array1)

    def hands_down(self,time,count):
        pwm_array1 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array1)

    def move_forward(self,time,count):
        for x in range(count):
            pwm_array1 = [0, 0, 110, 100, 160, 180, 110, 100, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array2 = [0, 0, 110, 90, 180, 180, 110, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array3 = [20, 0, 75, 80, 180, 180, 70, 80, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array4 = [0, 0, 75, 90, 180, 180, 70, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            self.servo.moveservo(time, pwm_array1)
            self.servo.moveservo(time, pwm_array2)
            self.servo.moveservo(time, pwm_array3)
            self.servo.moveservo(time, pwm_array4)
        pwm_array5 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array5)

    def move_backward(self,time,count):
        for x in range(count):
            pwm_array1 = [0, 0, 110, 80, 180, 180, 110, 80, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array2 = [0, 0, 110, 90, 180, 180, 110, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array3 = [0, 0, 70, 100, 180, 180, 70, 100, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array4 = [0, 0, 70, 90, 180, 180, 70, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            self.servo.moveservo(time, pwm_array1)
            self.servo.moveservo(time, pwm_array2)
            self.servo.moveservo(time, pwm_array3)
            self.servo.moveservo(time, pwm_array4)
        pwm_array5 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array5)
        
    def turn_left(self,time,count):
        for x in range(count):
            pwm_array1 = [0, 0, 90, 90, 180, 180, 90, 75, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array2 = [0, 0, 90, 75, 180, 180, 90, 75, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array3 = [0, 0, 110, 75, 180, 180, 90, 75, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array4 = [0, 0, 110, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array5 = [0, 0, 110, 105, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array6 = [0, 0, 110, 105, 180, 180, 90, 105, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array7 = [0, 0, 90, 105, 180, 180, 90, 105, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array8 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            self.servo.moveservo(time, pwm_array1)
            self.servo.moveservo(time, pwm_array2)
            self.servo.moveservo(time, pwm_array3)
            self.servo.moveservo(time, pwm_array4)
            self.servo.moveservo(time, pwm_array5)
            self.servo.moveservo(time, pwm_array6)
            self.servo.moveservo(time, pwm_array7)
            self.servo.moveservo(time, pwm_array8)
        pwm_array9 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array9)

    def turn_right(self,time,count):
        for x in range(count):
            pwm_array1 = [0, 0, 90, 105, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array2 = [0, 0, 90, 105, 180, 180, 90, 105, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array3 = [0, 0, 90, 105, 180, 180, 70, 105, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array4 = [0, 0, 90, 90, 180, 180, 70, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array5 = [0, 0, 90, 90, 180, 180, 70, 75, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array6 = [0, 0, 90, 75, 180, 180, 70, 75, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array7 = [0, 0, 90, 75, 180, 180, 90, 75, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array8 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            self.servo.moveservo(time, pwm_array1)
            self.servo.moveservo(time, pwm_array2)
            self.servo.moveservo(time, pwm_array3)
            self.servo.moveservo(time, pwm_array4)
            self.servo.moveservo(time, pwm_array5)
            self.servo.moveservo(time, pwm_array6)
            self.servo.moveservo(time, pwm_array7)
            self.servo.moveservo(time, pwm_array8)
        pwm_array9 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array9)

    def side_move_right(self,time,count):
        for x in range(count):
            pwm_array1 = [0, 30, 90, 90, 180, 180, 90, 130, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array2 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            self.servo.moveservo(time, pwm_array1)
            self.servo.moveservo(time, pwm_array2)     
        pwm_array5 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array5)

    def side_move_left(self,time,count):
        for x in range(count):
            pwm_array1 = [0, 0, 90, 50, 180, 150, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array2 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            self.servo.moveservo(time, pwm_array1)
            self.servo.moveservo(time, pwm_array2)     
        pwm_array5 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array5)

    def flying_move(self,time,count):
        pwm_array1 = [0, 120, 90, 90, 180, 60, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time*2, pwm_array1)
        for x in range(count):
            pwm_array2 = [0, 60, 90, 120, 180, 120, 90, 60, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array3 = [0, 120, 90, 90, 180, 60, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            self.servo.moveservo(time, pwm_array2)
            self.servo.moveservo(time, pwm_array3)     
        pwm_array4 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time*2, pwm_array4)

    def leg_shake(self,time,count):
        for x in range(count):
            pwm_array1 = [0, 30, 90, 75, 180, 150, 90, 75, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array2 = [0, 0, 90, 105, 180, 180, 90, 105, 90, 90, 90, 90, 90, 90, 90, 90]
            self.servo.moveservo(time, pwm_array1)
            self.servo.moveservo(time, pwm_array2)     
        pwm_array3 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array3)

    def hand_straight_shake(self,time,count):
        pwm_array1 = [160, 0, 90, 90, 90, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array1)
        for x in range(count):
            pwm_array2 = [90, 0, 90, 90, 20, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array3 = [160, 0, 90, 90, 90, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            self.servo.moveservo(time, pwm_array2)
            self.servo.moveservo(time, pwm_array3)     
        pwm_array4 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array4)

    def leg_head_shake(self,time,count):
        for x in range(count):
            pwm_array1 = [0, 0, 110, 90, 180, 180, 110, 90, 110, 90, 90, 90, 90, 90, 90, 90]
            pwm_array2 = [0, 0, 70, 90, 180, 180, 70, 90, 70, 90, 90, 90, 90, 90, 90, 90]
            self.servo.moveservo(time, pwm_array1)
            self.servo.moveservo(time, pwm_array2)     
        pwm_array3 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array3)

    def jump(self,time,count):
        for x in range(count):
            pwm_array1 = [0, 60, 90, 120, 180, 120, 90, 60, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array2 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            self.servo.moveservo(time, pwm_array1)
            self.servo.moveservo(time, pwm_array2)     
        pwm_array3 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array3)
        
    def right_slide_wave(self,time,count):
        pwm_array1 = [0, 0, 90, 90, 180, 180, 90, 60, 90, 90, 90, 90, 90, 90, 90, 90]
        pwm_array2 = [0, 90, 90, 60, 180, 90, 90, 60, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array1)
        self.servo.moveservo(time, pwm_array2)
        for x in range(count):
            pwm_array3 = [0, 120, 90, 60, 180, 60, 90, 60, 120, 90, 90, 90, 90, 90, 90, 90]
            pwm_array4 = [0, 60, 90, 60, 180, 120, 90, 60, 60, 90, 90, 90, 90, 90, 90, 90]
            self.servo.moveservo(time, pwm_array3)
            self.servo.moveservo(time, pwm_array4)     
        pwm_array5 = [0, 0, 90, 90, 180, 180, 90, 60, 90, 90, 90, 90, 90, 90, 90, 90]
        pwm_array6 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array5)
        self.servo.moveservo(time, pwm_array6)
        
    def left_slide_wave(self,time,count):
        pwm_array1 = [0, 0, 90, 120, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        pwm_array2 = [0, 90, 90, 120, 180, 90, 90, 120, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array1)
        self.servo.moveservo(time, pwm_array2)
        for x in range(count):
            pwm_array3 = [0, 120, 90, 120, 180, 60, 90, 120, 60, 90, 90, 90, 90, 90, 90, 90]
            pwm_array4 = [0, 60, 90, 120, 180, 120, 90, 120, 120, 90, 90, 90, 90, 90, 90, 90]
            self.servo.moveservo(time, pwm_array3)
            self.servo.moveservo(time, pwm_array4)     
        pwm_array5 = [0, 0, 90, 120, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        pwm_array6 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array5)
        self.servo.moveservo(time, pwm_array6)

    def right_hand_balance(self,time,count):
        pwm_array1 = [0, 60, 90, 90, 180, 180, 90, 60, 90, 90, 90, 90, 90, 90, 90, 90]
        pwm_array2 = [0, 60, 90, 40, 180, 120, 90, 60, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array1)
        self.servo.moveservo(time*2, pwm_array2)
        for x in range(count):
            pwm_array3 = [0, 60, 90, 40, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array4 = [0, 60, 90, 40, 180, 120, 90, 60, 90, 90, 90, 90, 90, 90, 90, 90]
            self.servo.moveservo(time/2, pwm_array3)
            self.servo.moveservo(time/2, pwm_array4)     
        pwm_array5 = [0, 60, 90, 90, 180, 180, 90, 60, 90, 90, 90, 90, 90, 90, 90, 90]
        pwm_array6 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time*2, pwm_array5)
        self.servo.moveservo(time, pwm_array6)
        
    def left_hand_balance(self,time,count):
        pwm_array1 = [0, 0, 90, 120, 180, 120, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        pwm_array2 = [0, 60, 90, 120, 180, 120, 90, 140, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array1)
        self.servo.moveservo(time*2, pwm_array2)
        for x in range(count):
            pwm_array3 = [0, 90, 90, 90, 180, 120, 90, 140, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array4 = [0, 60, 90, 120, 180, 120, 90, 140, 90, 90, 90, 90, 90, 90, 90, 90]
            self.servo.moveservo(time/2, pwm_array3)
            self.servo.moveservo(time/2, pwm_array4)     
        pwm_array5 = [0, 0, 90, 120, 180, 120, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        pwm_array6 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time*2, pwm_array5)
        self.servo.moveservo(time, pwm_array6)
        
    def side_shake(self,time,count):
        for x in range(count):
            pwm_array1 = [0, 60, 90, 60, 180, 120, 90, 60, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array2 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array3 = [0, 60, 90, 120, 180, 120, 90, 120, 90, 90, 90, 90, 90, 90, 90, 90]
            pwm_array4 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
            self.servo.moveservo(time, pwm_array1)
            self.servo.moveservo(time, pwm_array2)
            self.servo.moveservo(time, pwm_array3)
            self.servo.moveservo(time, pwm_array4)
        pwm_array5 = [0, 0, 90, 90, 180, 180, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
        self.servo.moveservo(time, pwm_array5)
        
        
