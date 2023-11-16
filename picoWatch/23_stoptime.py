import utime
import RP
LCD = RP.LCD_1inch28()

LCD.fill_rect(0,0,240,40,LCD.red)
LCD.text("Now",110,25,LCD.white)
LCD.show()

N1 = utime.ticks_ms()
utime.sleep(1)
N2 = utime.ticks_ms()

LCD.text(str(N2-N1),100,120,LCD.black)
LCD.show()
