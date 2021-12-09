from machine import Pin, I2C
import time
import machine
import ssd1306

# using default address 0x3C
i2c = machine.I2C(1, scl = machine.Pin(22), sda = machine.Pin(21), freq = 400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
for i in range(51):
    oled.fill_rect(0, 0, 32, 54, 1)
    oled.fill_rect(2, 2, 28, (50 - i), 0)
    oled.text((str(i*2)+'%'), 2, 57, 1)
    oled.fill_rect(90, 0, 32, 54, 1)
    oled.fill_rect(92, 2, 28, i, 0)
    oled.text((str((50-i)*2)+'%'), 95, 57, 1)
    oled.show()
    oled.fill(0)
    time.sleep(1)
    
for i in range(50, -1, -1):
    oled.fill_rect(0, 0, 32, 54, 1)
    oled.fill_rect(2, 2, 28, (50 - i), 0)
    oled.text((str(i*2)+'%'), 4, 57, 1)
    oled.fill_rect(90, 0, 32, 54, 1)
    oled.fill_rect(92, 2, 28, i, 0)
    oled.text((str((50-i)*2)+'%'), 95, 57, 1)
    oled.show()
    oled.fill(0)
    time.sleep(1)
