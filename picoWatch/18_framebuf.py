from machine import Pin,I2C,SPI,PWM,ADC
import RP,framebuf

LCD = RP.LCD_1inch28()
LCD.set_bl_pwm(65535)

heart_data = bytearray(b'\xF8\x00\xE3\xC0\xC1\xE0\x07\xF0\x0F\xF8\x1E\x7C\x3C\x3E\x78\x1F\xF0\x0F\xE0\x07\xC0\x03\x80\x01\x00')

converted_data = bytearray()
for i in range(0, len(heart_data), 2):
    pixel = (heart_data[i] << 8) | heart_data[i + 1]
    converted_data.append((pixel >> 8) & 0xFF)  # 高字节
    converted_data.append(pixel & 0xFF)         # 低字节

heart_width = 8
heart_height = 11

x_position = (240 - heart_width) // 2
y_position = (240 - heart_height) // 2

for y in range(heart_height):
    start_index = y * heart_width
    end_index = start_index + heart_width
    self.buffer[(y_position + y) * self.width + x_position: (y_position + y) * self.width + x_position + heart_width] = converted_data[start_index:end_index]
fb = framebuf.FrameBuffer(pic, 240, 240, framebuf.RGB565)
LCD.blit(fb,60,60)
LCD.show()