import framebuf
import time
import gc
from middle_state import middle_state
from my_text import my_text
from machine import Timer
FPS = 24
refresh_timing = int(1000/FPS)
blue=32620

def main_menu(display, my_input,fbuf):
    from musics import mario_song
    bgm_timer = Timer(period=40, callback=lambda t:mario_song.tick())
    print(gc.mem_free())
    #fbuf = framebuf.FrameBuffer(bytearray(240 * 180 * 2), 240, 180, framebuf.RGB565)
    with open('images/main_menu_bg.bin', 'rb') as f:
            for i in range(180):
                fbuf.blit(framebuf.FrameBuffer(bytearray(f.read(480)), 240, 1, framebuf.RGB565),0, i)
    
    with open('images/title_page_mushroom.bin', 'rb') as f:
        mushroom = framebuf.FrameBuffer(bytearray(f.read(128)), 8, 8, framebuf.RGB565)
    coins = []
    with open('images/coin-0-1.bin', 'rb') as f:
        coins.append(framebuf.FrameBuffer(bytearray(f.read(80)), 5, 8, framebuf.RGB565))
    with open('images/coin-0-2.bin', 'rb') as f:
        coins.append(framebuf.FrameBuffer(bytearray(f.read(80)), 5, 8, framebuf.RGB565))
    with open('images/coin-0-3.bin', 'rb') as f:
        coins.append(framebuf.FrameBuffer(bytearray(f.read(80)), 5, 8, framebuf.RGB565))
    with open('images/coin-0-2.bin', 'rb') as f:
        coins.append(framebuf.FrameBuffer(bytearray(f.read(80)), 5, 8, framebuf.RGB565))
    frame_timing = 1
    frame = 0
    player = 1
    
    display.blit_buffer(fbuf, 0, 30, 240, 180)
    while True:
        start_time = time.ticks_ms()
        fbuf.fill_rect(0,0,80,8,blue)
        fbuf.fill_rect(56,107,8,21,blue)
        fbuf.text(f'FPS:{int(1000/(frame_timing))}', 0, 0)
        
        fbuf.blit(mushroom, 56, 95+12*player, 7160)
        
        fbuf.blit(coins[frame//4%4], 76, 15, 65535)
        my_text(fbuf, 'mario', 16, 8)
        my_text(fbuf, '000000', 16, 16)
        my_text(fbuf, 'x00', 88, 16)
        my_text(fbuf, 'world', 132, 8)
        my_text(fbuf, '1-1', 140, 16)
        my_text(fbuf, 'time', 192, 8)
        my_text(fbuf, '1 player game', 72, 108)
        my_text(fbuf, '2 player game', 72, 120)
        my_text(fbuf, 'top - 000000', 76, 136)
        display.blit_buffer(fbuf, 0, 30, 240, 180)
        
        
        if(my_input.y()==1):
            player=2
        elif(my_input.y()==-1):
            player=1
        if(my_input.A()):
            mario_song.stop()
            bgm_timer.deinit()
            return
        
        frame_timing = time.ticks_ms()-start_time
        if(frame_timing<refresh_timing):
            time.sleep_ms(refresh_timing - frame_timing)
            frame_timing = refresh_timing
        frame+=1

def main(display, my_input):
    print(gc.mem_free())
    fbuf = framebuf.FrameBuffer(bytearray(240 * 180 * 2), 240, 180, framebuf.RGB565)
    main_menu(display, my_input,fbuf)
    print(gc.mem_free())
    gc.collect()
    print(gc.mem_free())
    middle_state(display, my_input,fbuf)
    gc.collect()
    print(gc.mem_free())
    
    
    
if __name__ == "__main__":
    import st7789_backup as st77899
    from st7789 import ST7789
    from machine import Pin, ADC, SPI
    from my_input import Input
    disp_width = 240
    disp_height = 240
    spi_sck=Pin(2)
    spi_tx=Pin(3)
    st7789_res = 0
    st7789_dc  = 1
    spi0=SPI(0,baudrate=62500000, phase=1, polarity=1, sck=spi_sck, mosi=spi_tx)
    print(spi0)
    player=1
    display1 = st77899.ST7789(spi0, 240, 240,
                              reset=Pin(st7789_res, Pin.OUT),
                              dc=Pin(st7789_dc, Pin.OUT),
                              xstart=0, ystart=0, rotation=0)

    display = ST7789(spi0,disp_width,disp_height,
                              dc=Pin(st7789_dc, Pin.OUT),
                              reset=Pin(st7789_res, Pin.OUT),
                              rotation=0)
    display1.pixel(0,0,0)#magic code!!!
    del(display1)
    main(display, Input())
