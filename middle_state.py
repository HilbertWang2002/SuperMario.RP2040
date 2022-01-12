import framebuf
import time
from my_text import my_text
FPS = 24
refresh_timing = int(1000/FPS)

def middle_state(display, my_input):
    frame_timing = 1
    frame = 0
    with open('images/mario_normal.bin', 'rb') as f:
        mario_normal = framebuf.FrameBuffer(bytearray(f.read(384)), 12, 16, framebuf.RGB565)
    fbuf = framebuf.FrameBuffer(bytearray(240 * 180 * 2), 240, 180, framebuf.RGB565)
    fbuf.fill(0)
    with open('images/font.bin', 'rb') as f:
        font = f.read(4992)
    coins = []
    with open('images/coin-0-1.bin', 'rb') as f:
        coins.append(framebuf.FrameBuffer(bytearray(f.read(80)), 5, 8, framebuf.RGB565))
    with open('images/coin-0-2.bin', 'rb') as f:
        coins.append(framebuf.FrameBuffer(bytearray(f.read(80)), 5, 8, framebuf.RGB565))
    with open('images/coin-0-3.bin', 'rb') as f:
        coins.append(framebuf.FrameBuffer(bytearray(f.read(80)), 5, 8, framebuf.RGB565))
    with open('images/coin-0-2.bin', 'rb') as f:
        coins.append(framebuf.FrameBuffer(bytearray(f.read(80)), 5, 8, framebuf.RGB565))
    with open('images/font.bin', 'rb') as f:
        font = f.read(4992)
    while True:
        start_time = time.ticks_ms()
        fbuf.fill_rect(0,0,80,8,0)
        fbuf.text(f'FPS:{int(1000/(frame_timing))}', 0, 0)
        
        
        fbuf.blit(coins[frame//4%4], 76, 15, 65535)
        fbuf.blit(mario_normal, 80, 114, 65535)
        my_text(fbuf, 'mario', 16, 8, font)
        my_text(fbuf, '000000', 16, 16, font)
        my_text(fbuf, 'x00', 88, 16, font)
        my_text(fbuf, 'world', 132, 8, font)
        my_text(fbuf, '1-1', 140, 16, font)
        my_text(fbuf, 'time', 192, 8, font)
        my_text(fbuf, 'world  1-1', 72, 96, font)
        my_text(fbuf, 'x  1', 108, 120, font)
        display.blit_buffer(fbuf, 0, 30, 240, 180)
        
        frame_timing = time.ticks_ms()-start_time
        if(frame_timing<refresh_timing):
            time.sleep_ms(refresh_timing - frame_timing)
            frame_timing = refresh_timing
        frame+=1
    
    