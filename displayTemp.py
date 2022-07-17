from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd
from machine import Pin, I2C
import utime as time
from dht import DHT11, InvalidChecksum

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
while True:
    print(I2C_ADDR)
    lcd.blink_cursor_on()
    pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    t  = (sensor.temperature)
    h = (sensor.humidity)
    lcd.putstr("Temperature:{}".format(sensor.temperature))
    lcd.putstr("Humidity:{}".format(sensor.humidity))
    #lcd.putstr("Im alive")
    sleep(10)
    lcd.clear()
