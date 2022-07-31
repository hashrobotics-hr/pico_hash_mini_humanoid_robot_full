from pca9685 import PCA9685
from machine import I2C, Pin
from servo import Servos



sda = Pin(0)
scl = Pin(1)
id = 0
i2c = I2C(0, sda=sda, scl=scl)

pca = PCA9685(i2c=i2c)
servo = Servos(i2c=i2c)
servo.position(index=0, degrees=90)

