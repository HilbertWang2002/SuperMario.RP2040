import uos
from machine import Pin, ADC, Timer, SPI
import st7789_backup as st77899
import st7789
from st7789 import color565
from fonts import vga2_8x8 as font1
from fonts import vga1_16x32 as font2
import time
import mario_main
from my_input import Input

st7789_res = 0
st7789_dc  = 1
disp_width = 240
disp_height = 240
spi_sck=Pin(2)
spi_tx=Pin(3)
spi0=SPI(0,baudrate=62500000, phase=1, polarity=1, sck=spi_sck, mosi=spi_tx)


game='Train No.7'
choose_game=False

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

display2.fill_rect(0,0,240,240,color565(0,0,0))
display2.fill_rect(30,70,180,30,color565(45,200,45))
display2.fill_rect(30,140,180,30,color565(45,200,45))
display2.rect(30,70,180,30,color565(255,255,255))
display2.text(font1,"Train No.7",80,80,color565(255,255,255),color565(45,200,45))
display2.text(font1,"Super Mario",78,150,color565(255,255,255),color565(45,200,45))

my_input = Input()
while choose_game==False:
    if my_input.y()==1:
        display2.rect(30,70,180,30,color565(45,200,45))
        display2.rect(30,140,180,30,color565(255,255,255))
        game='Super Mario'
    elif my_input.y()==-1:
        display2.rect(30,70,180,30,color565(255,255,255))
        display2.rect(30,140,180,30,color565(45,200,45))
        game='Train No.7'
    if my_input.A():
        choose_game=True
        
display2.fill_rect(0,0,240,240,0)
if (game=='Train No.7'):
    #game_main.main(display2, my_input)
    pass
elif(game=='Super Mario'):
    mario_main.main(display2, my_input)