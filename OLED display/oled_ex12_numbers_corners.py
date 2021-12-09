from machine import Pin, I2C
import time
import machine
import ssd1306

# using default address 0x3C
i2c = machine.I2C(1, scl = machine.Pin(22), sda = machine.Pin(21), freq = 400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)


for i in range (51):
    oled.text(str(i), 0, 0, 1)
    oled.text(str(51 - i), 110, 0, 1)
    oled.text(str(i ** (1/2)), 0, 55, 1)
    oled.text(str(-51 + i), 104, 55, 1)
    oled.show()
    oled.fill(0)
    time.sleep(1)