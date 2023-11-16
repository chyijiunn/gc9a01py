from machine import Pin, SPI
import gc9a01py as gc9a01
from fonts.romfonts import vga2_16x32 as font

spi = SPI(1, baudrate=62500000, sck=Pin(10), mosi=Pin(11))
LCD = gc9a01.GC9A01(spi,dc=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),reset=Pin(12, Pin.OUT),backlight=Pin(25, Pin.OUT),rotation=0)
color = gc9a01.color565

LCD.fill(gc9a01.YELLOW)
LCD.text(font,"RP2040-LCD-1.28",40,25,color(23,232,0),color(23,100,100))#字型、字串、x ,y,前景色、背景色