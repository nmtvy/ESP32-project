import machine, onewire, ds18x20, time
from machine import Pin, SoftI2C
from time import sleep
import machine
import ssd1306

i2c2 = machine.I2C(1, scl = machine.Pin(22), sda = machine.Pin(21), freq = 400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c2)
ds_pin = machine.Pin(15)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms = ds_sensor.scan()
print('Found DS devices: ', roms)

while True:
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  for rom in roms:
    print(rom)
    print(ds_sensor.read_temp(rom))
  time.sleep(0.2)
  oled.fill(0)
  oled.text('Temperature:'+ str(ds_sensor.read_temp(rom)) + '°C', 0, 2, 1)
  oled.show()