from machine import Pin, I2C
from machine import ADC
import time
import machine
import ssd1306
import dht 

sensor = dht.DHT11(Pin(14))

# using default address 0x3C
i2c = machine.I2C(1, scl = machine.Pin(22), sda = machine.Pin(21), freq = 400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    for i in range (125):
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        time.sleep(1)
        oled.fill(0)
        oled.text('Temperature: '+ str(temp) + 'C', 0, 2, 1)
        oled.text('Humidity: '+str(hum)+'%', 0, 20, 1)
        oled.text('--by Vy--', i, 50, 1)
        oled.show()
    

    
