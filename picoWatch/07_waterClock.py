import time
import RP
LCD = RP.LCD_1inch28()
LCD.set_bl_pwm(65535)

while 1:
    LCD.fill_rect(80,120,80,10,LCD.white)
    now = list(time.localtime())
    sec = now[5]
    LCD.fill_rect(0,0,240,236-(4*sec),LCD.white)
    LCD.fill_rect(0,236-(4*sec),240,240,0x180f)
    
    LCD.text(str(now[3])+':'+str(int(now[4])),100,120,LCD.black)

    LCD.show()
    time.sleep(0.9)


