import framebuf
import time
def main_menu(display, ipt):
    fbuf = framebuf.FrameBuffer(bytearray(240 * 180 * 2), 240, 180, framebuf.RGB565)
    start_time = time.ticks_ms()
    while True:
        print(1)
        #fbuf.fill(color565(255,255,255))
        with open('images/main_menu_bg.bin', 'rb') as f:
            for i in range(18):
                fbuf.blit(framebuf.FrameBuffer(bytearray(f.read(4800)), 240, 10, framebuf.RGB565),0, 10*i)
        fbuf.text(f'FPS:{int(1000/(time.ticks_ms()-start_time))}', 0, 0)
        #print(time.ticks_ms()-start_time)
        display.blit_buffer(fbuf, 0, 30, 240, 180)
        #print(time.ticks_ms()-start_time)
        start_time = time.ticks_ms()
    
def main(display, ipt):
    main_menu(display, ipt)
    
    
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