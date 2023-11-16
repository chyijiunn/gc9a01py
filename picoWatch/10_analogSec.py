import time , RP, math

LCD = RP.LCD_1inch28()
LCD.set_bl_pwm(65535)

while 1:
    LCD.fill_rect(0,0,240,240,LCD.white)
    now = list(time.localtime())
    #second
    sec = now[5] * 6#sec/60*360
    radian = math.radians(sec)
    x_sin = math.sin(radian)
    y_cos = math.cos(radian)
    LCD.line(120,120,int(120*x_sin+120),int(-120*y_cos+120),LCD.red)
    
    #minute
    minute = now[4] * 6#min/60*360
    radian = math.radians(minute)
    x_sin = math.sin(radian)
    y_cos = math.cos(radian)
    LCD.line(120,120,int(110*x_sin+110),int(-110*y_cos+110),LCD.black)
    
    LCD.show()
    time.sleep(1)
    




