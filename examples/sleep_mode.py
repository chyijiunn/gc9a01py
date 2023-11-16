import random
from machine import Pin, SPI
import gc9a01py as gc9a01
from time import sleep
spi = SPI(1, baudrate=100_000_000, sck=Pin(10), mosi=Pin(11))
lcd = gc9a01.GC9A01(spi,dc=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),reset=Pin(12, Pin.OUT),backlight=Pin(25, Pin.OUT),        rotation=0)

lcd.fill(gc9a01.BLUE)
sleep(1)
lcd.sleep_mode(True)
sleep(1)
lcd.sleep_mode(False)

