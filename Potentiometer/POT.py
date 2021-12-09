# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, ADC, PWM, I2C
from time import sleep
import machine
import ssd1306
import time


led = PWM(Pin(15),5000)
pot = ADC(Pin(36))
pot.width(ADC .WIDTH_9BIT)
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v
i2c = machine.I2C(1, scl = machine.Pin(22), sda = machine.Pin(21), freq = 400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    pot_value = pot.read()
    print(pot_value)
    led.duty(pot_value)
    n = round(pot_value/511*100)
    print(n)
    time.sleep(0.5)

