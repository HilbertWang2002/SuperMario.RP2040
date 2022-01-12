import uos
from machine import Pin, ADC, Timer, SPI
import st7789_backup as st77899
import st7789
from st7789 import color565
from fonts import vga2_8x8 as font1
from fonts import vga1_16x32 as font2
import time
import game_main
from my_input import Input

st7789_res = 0
st7789_dc  = 1
disp_width = 240
disp_height = 240
spi_sck=Pin(2)
spi_tx=Pin(3)
spi0=SPI(0,baudrate=62500000, phase=1, polarity=1, sck=spi_sck, mosi=spi_tx)


game=None

display = st77899.ST7789(spi0, disp_width, disp_width,
                          reset=machine.Pin(st7789_res, machine.Pin.OUT),
                          dc=machine.Pin(st7789_dc, machine.Pin.OUT),
                          xstart=0, ystart=0, rotation=0)

display2 = st7789.ST7789(spi0,disp_width,disp_height,
                          dc=machine.Pin(st7789_dc, machine.Pin.OUT),
                          reset=machine.Pin(st7789_res, machine.Pin.OUT),
                          rotation=0)

display.text(font2, "Welcome!", 60, 110)
del(display)
time.sleep(1)

display2.fill_rect(0,0,240,240,color565(30,67,131))
display2.fill_rect(0,0,240,12,color565(100,23,45))
time.sleep(1)
display2.fill_rect(0,0,240,240,0)


my_input = Input()
game_main.main(display2, my_input)