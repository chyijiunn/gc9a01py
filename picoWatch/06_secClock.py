import time
import RP
LCD = RP.LCD_1inch28()
LCD.set_bl_pwm(65535)

while 1:
    now = list(time.localtime())
    sec = now[5]
    LCD.fill_rect(0,0,240,236-(4*sec),LCD.white)
    LCD.fill_rect(0,236-(4*sec),240,4,0x180f)
    LCD.fill_rect(80,120,80,10,LCD.white)
    LCD.text(str(sec),110,120,LCD.black)

    LCD.show()
    time.sleep(1)

