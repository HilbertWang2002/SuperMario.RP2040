import framebuf
import time
FPS = 50
refresh_timing = int(1000/FPS)
blue=32620
def color565(red,green=0,blue=0):
    try:
        red,green,blue=red
    except TypeError:
        pass
    return (red & 0xf8) << 8 | (green & 0xfc) << 3 | blue >> 3
def main_menu(display, my_input):
    fbuf = framebuf.FrameBuffer(bytearray(240 * 180 * 2), 240, 180, framebuf.RGB565)
    with open('images/main_menu_bg.bin', 'rb') as f:
            for i in range(18):
                fbuf.blit(framebuf.FrameBuffer(bytearray(f.read(4800)), 240, 10, framebuf.RGB565),0, 10*i)
    display.blit_buffer(fbuf, 0, 30, 240, 180)
    frame_timing = 1
    while True:
        start_time = time.ticks_ms()
        fbuf.fill_rect(0,0,80,8,blue)
        fbuf.text(f'FPS:{int(1000/(frame_timing))}', 0, 0)
        display.blit_buffer(fbuf, 0, 30, 240, 180)
        start_time = time.ticks_ms()
        
        if(my_input.y()==1):
            player=2
        elif(my_input.y()==-1):
            player=1
        if(my_input.A()):
            break
        frame_timing = time.ticks_ms()-start_time
        if(frame_timing<refresh_timing):
            time.sleep_ms(refresh_timing - frame_timing)
            frame_timing = refresh_timing
def main(display, my_input):
    main_menu(display, my_input)
    
    
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
