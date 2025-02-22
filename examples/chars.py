"""
chars.py

    Pages through all characters of four fonts on the display.

"""
import utime
from machine import Pin, SPI
import gc9a01py as gc9a01

# Choose a few fonts

# from fonts.romfonts import vga1_8x8 as font
from fonts.romfonts import vga2_8x8 as font1
# from fonts.romfonts import vga1_8x16 as font
from fonts.romfonts import vga2_8x16 as font2
# from fonts.romfonts import vga1_16x16 as font
# from fonts.romfonts import vga1_bold_16x16 as font
# from fonts.romfonts import vga2_16x16 as font
from fonts.romfonts import vga2_bold_16x16 as font3
# from fonts.romfonts import vga1_16x32 as font
# from fonts.romfonts import vga1_bold_16x32 as font
# from fonts.romfonts import vga2_16x32 as font
from fonts.romfonts import vga2_bold_16x32 as font4

def main():
    spi = SPI(1, baudrate=100_000_000, sck=Pin(10), mosi=Pin(11))
    tft = gc9a01.GC9A01(
        spi,
        dc=Pin(8, Pin.OUT),
        cs=Pin(9, Pin.OUT),
        reset=Pin(12, Pin.OUT),
        backlight=Pin(25, Pin.OUT),
        rotation=0)

    while True:
        for font in (font1, font2, font3, font4):
            tft.fill(gc9a01.BLUE)
            line = 0
            col = 0

            for char in range(font.FIRST, font.LAST):
                tft.text(font, chr(char), col, line, gc9a01.WHITE, gc9a01.BLUE)
                col += font.WIDTH
                if col > tft.width - font.WIDTH:
                    col = 0
                    line += font.HEIGHT

                    if line > tft.height-font.HEIGHT:
                        utime.sleep(3)
                        tft.fill(gc9a01.BLUE)
                        line = 0
                        col = 0

            utime.sleep(3)


main()
