"""
lines.py

    Draws lines and rectangles in random colors at random locations on the
    display.

"""
import random
from machine import Pin, SPI
import gc9a01py as gc9a01

def main():
    spi = SPI(1, baudrate=100_000_000, sck=Pin(10), mosi=Pin(11))
    tft = gc9a01.GC9A01(
        spi,
        dc=Pin(8, Pin.OUT),
        cs=Pin(9, Pin.OUT),
        reset=Pin(12, Pin.OUT),
        backlight=Pin(25, Pin.OUT),
        rotation=0)

    tft.fill(gc9a01.BLACK)

    while True:
        tft.line(
            random.randint(0, tft.width),
            random.randint(0, tft.height),
            random.randint(0, tft.width),
            random.randint(0, tft.height),
            gc9a01.color565(
                random.getrandbits(8),
                random.getrandbits(8),
                random.getrandbits(8)
                )
            )

        width = random.randint(0, tft.width // 2)
        height = random.randint(0, tft.height // 2)
        col = random.randint(0, tft.width - width)
        row = random.randint(0, tft.height - height)
        tft.fill_rect(
            col,
            row,
            width,
            height,
            gc9a01.color565(
                random.getrandbits(8),
                random.getrandbits(8),
                random.getrandbits(8)
            )
        )


main()
