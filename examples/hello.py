"""
hello.py

    Writes "Hello!" in random colors at random locations on the display

"""
import random
from machine import Pin, SPI
import gc9a01py as gc9a01

# Choose a font

# from fonts.romfonts import vga1_8x8 as font
# from fonts.romfonts import vga2_8x8 as font
# from fonts.romfonts import vga1_8x16 as font
# from fonts.romfonts import vga2_8x16 as font
# from fonts.romfonts import vga1_16x16 as font
# from fonts.romfonts import vga1_bold_16x16 as font
# from fonts.romfonts import vga2_16x16 as font
# from fonts.romfonts import vga2_bold_16x16 as font
# from fonts.romfonts import vga1_16x32 as font
# from fonts.romfonts import vga1_bold_16x32 as font
# from fonts.romfonts import vga2_16x32 as font
from fonts.romfonts import vga2_16x32 as font

def main():
    spi = SPI(1, baudrate=62500000, sck=Pin(10), mosi=Pin(11))
    LCD = gc9a01.GC9A01(spi,dc=Pin(8, Pin.OUT),cs=Pin(9, Pin.OUT),reset=Pin(12, Pin.OUT),backlight=Pin(25, Pin.OUT),rotation=0)
    color = gc9a01.color565

    while True:
        for rotation in range(4):
            LCD.rotation(rotation)
            LCD.fill(0)
            col_max = LCD.width - font.WIDTH*6
            row_max = LCD.height - font.HEIGHT

            for _ in range(12):
                LCD.text(font,"Trunking!",random.randint(0, col_max),random.randint(0, row_max),color(random.getrandbits(8),random.getrandbits(8),random.getrandbits(8)),color(random.getrandbits(8),random.getrandbits(8), random.getrandbits(8)))
main()