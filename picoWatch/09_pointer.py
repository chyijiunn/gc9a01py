import time , RP, math

LCD = RP.LCD_1inch28()
LCD.set_bl_pwm(65535)

while 1:
    now = list(time.localtime())
    sec = now[5] * 6#sec/60*360
    radian = math.radians(sec)
    x_sin = math.sin(radian)
    y_cos = math.cos(radian)
    LCD.line(120,120,int(120*x_sin+120),int(-120*y_cos+120),LCD.black)
    LCD.show()
    LCD.line(120,120,int(120*x_sin+120),int(-120*y_cos+120),LCD.white)
    print(now[5])