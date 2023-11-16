from machine import Pin, SPI
from fonts.romfonts import vga2_8x8 as font
import time
import gc9a01py as gc9a01

spi = SPI(1, baudrate=62500000, sck=Pin(10), mosi=Pin(11))
LCD = gc9a01.GC9A01(spi,dc=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),reset=Pin(12, Pin.OUT),backlight=Pin(25, Pin.OUT),rotation=0)
color = gc9a01.color565

LCD.fill(0)
LCD.fill_rect(0,0,40,4,color(255,0,0))
now = time.localtime()
LCD.text(font,str(now),0,120,color(255,255,255),0)