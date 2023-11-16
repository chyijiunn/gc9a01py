import time , RP, math

LCD = RP.LCD_1inch28()
LCD.set_bl_pwm(65535)

def spin( tic , spinLen , color):
    now = list(time.localtime())
    x = spinLen*math.sin(math.radians(now[tic]*6))
    y = spinLen*math.cos(math.radians(now[tic]*6))
    LCD.line(120,120,int(spinLen+x),int(spinLen-y),color)

while 1:
    LCD.fill_rect(0,40,240,200,LCD.white)
    spin(5,120,LCD.red)
    spin(4,110,LCD.black)

    LCD.show()