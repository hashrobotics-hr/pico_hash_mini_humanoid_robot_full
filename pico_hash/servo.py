from pca9685 import PCA9685
import math
from time import sleep,ticks_ms


class Servos:
    
    #_servopos = [0]*16
    #_increment= [0]*16

    def __init__(self, i2c, address=0x40, freq=50, min_us=600, max_us=2400,
                 degrees=180):
        self.period = 1000000 / freq
        self.min_duty = self._us2duty(min_us)
        self.max_duty = self._us2duty(max_us)
        self.degrees = degrees
        self.freq = freq
        self.pca9685 = PCA9685(i2c, address)
        self.pca9685.freq(freq)
        self._servopos = [0]*16
        self._increment= [0]*16

    def _us2duty(self, value):
        return int(4095 * value / self.period)

    def position(self, index, degrees=None, radians=None, us=None, duty=None):
        span = self.max_duty - self.min_duty
        if degrees is not None:
            duty = self.min_duty + span * degrees / self.degrees
        elif radians is not None:
            duty = self.min_duty + span * radians / math.radians(self.degrees)
        elif us is not None:
            duty = self._us2duty(us)
        elif duty is not None:
            pass
        else:
            return self.pca9685.duty(index)
        duty = min(self.max_duty, max(self.min_duty, int(duty)))
        self.pca9685.duty(index, duty)

    def release(self, index):
        self.pca9685.duty(index, 0)

#Custom Added

        
    def setservo(self,index,degree):
        self.position(index=index, degrees=degree)
        
    def moveservo(self, time, targetangle):
        if(time > 10):
            for x in range(len(targetangle)):
                self._increment[x]=((targetangle[x]) - self._servopos[x]) / (time / 10)
            finaltime=ticks_ms()+time
            iteration=0
            while(ticks_ms()< finaltime):
                iteration=iteration+1
                partialtime = ticks_ms() + 10
                for y in range(len(targetangle)):
                    self.setservo(y, (int)(self._servopos[y] + (iteration * self._increment[y])))     
                while(ticks_ms() < partialtime):
                    pass
        else:
            for y in range(15):
                setservo(y, int(targetangle[y]))
        for z in range(16):
            self._servopos[z] = targetangle[z]
            
    def initial_position(self):
        _angarr=[0, 0, 90, 90, 180, 180, 90, 90, 90, 0, 0, 0, 0, 0, 0, 0] # RH1,RH2,RL1,RL2,LH1,LH2,LL1,LL2,HEAD,DMY1,DMY2,DMY3,DMY4,DMY5,DMY6
        for i in range (16):
            self._servopos[i]=_angarr[i]
        self.moveservo(2000, _angarr)
        
