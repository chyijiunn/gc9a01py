import time , RP, math , random
from machine import Timer
qmi8658=RP.QMI8658()
LCD = RP.LCD_1inch28()
LCD.set_bl_pwm(65535)
cx , cy =120 ,120 #center of watch

def spin( tic , spinLen , color):
    now = list(time.localtime())
    x = spinLen*math.sin(math.radians(now[tic]*6))
    y = spinLen*math.cos(math.radians(now[tic]*6))
    LCD.line(cx,cy,int(cx+x),int(cy-y),color)
    
def hourspin(spinLen , color):
    now = list(time.localtime())
    
    if now[3] < 12:hh = now[3]#切換24小時制 --> 12 小時制
    else : hh = now[3] - 12
    
    x = spinLen*math.sin(math.radians(hh*30+(now[4]/2))) #hour spin 30˚/h , +0.5˚/min
    y = spinLen*math.cos(math.radians(hh*30+(now[4]/2)))
    LCD.line(cx,cy,int(cx+x),int(cy-y),color)

def centerCircle(tic , spinLen , color):
    now = list(time.localtime())
    r = now[tic]*2
    for i in range(-r,r,1):
        for j in range(-r,r,1):
            if i*i + j*j <= r*r:
                LCD.pixel(cx+i,cy+j,color)
                
def runDotRing(tic , spinLen , color):
    r = 10
    now = list(time.localtime())
    x = int(spinLen*math.sin(math.radians(now[tic]*6)))
    y = int(spinLen*math.cos(math.radians(now[tic]*6)))
    for i in range(-r,r,1):
        for j in range(-r,r,1):
            if i*i + j*j <= r*r:
                LCD.pixel(cx+x+i,cy-y+j,color)
                
def color(R,G,B): # Convert RGB888 to RGB565
    return (((G&0b00011100)<<3) +((B&0b11111000)>>3)<<8) + (R&0b11111000)+((G&0b11100000)>>5)

def changeColor(tim):
    global R ,G ,B
    R = random.randint(-1,256)
    G = random.randint(-1,256)
    B = random.randint(-1,256)
    return R ,G ,B

def waterclock():
    now = list(time.localtime())
    sec = now[5]
    LCD.fill_rect(0,236-(4*sec),240,240,0x180f)
    LCD.text(str(now[3])+':'+str(int(now[4])),100,120,LCD.white)
    
tim = Timer(-1)
tim.init(period=60000, mode=Timer.PERIODIC, callback= changeColor)

R = random.randint(-1,256)
G = random.randint(-1,256)
B = random.randint(-1,256)
    
while 1:
    LCD.fill_rect(0,00,240,240,0)
    waterclock()
    #centerCircle(5,120,color(R,G,256-B))#秒
    #spin(5,120,color(R,256-G,256-B))#秒
    spin(4,100,color(256-R,256-G,256-B))#分
    hourspin(50 , color(256-R,256-G,B))#時
    runDotRing(5,110,color(256-R,G,256-B))
    
    LCD.show()
