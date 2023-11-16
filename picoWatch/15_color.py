from RP import *
LCD = LCD_1inch28()

def color(R,G,B): # Convert RGB888 to RGB565
    return (((G&0b00011100)<<3) +((B&0b11111000)>>3)<<8) + (R&0b11111000)+((G&0b11100000)>>5)

# 參考 coolors.co
print(color(37, 40, 61))
LCD.fill(5581)
LCD.show()

LCD.fill_rect(20,20,80,80,0)
LCD.show()
for i in range(100):
    LCD.scroll(2,2)
    time.sleep(0.01)
    LCD.show()


