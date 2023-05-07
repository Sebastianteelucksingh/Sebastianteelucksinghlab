from Lights import Light
from Buzzer import * 
from Displays import *

import time

print("Hello, Pi Pico!")

led = Light(25, "Onboard LED")

led.on()
time.sleep(0.5)
led.off()
time.sleep(0.5)

redled = Light(15, "red light")

redled.on()
time.sleep(2)
redled.off()
time.sleep(0.5)

buzz = PassiveBuzzer(14)
buzz.play()
time.sleep(1)
buzz.stop()

Display = LCDDisplay(sda=20, scl=21, i2cid = 0)
Display.showText("Life is good")