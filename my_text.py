import framebuf
font_map = {'0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'a': 10,
            'b': 11,
            'c': 12,
            'd': 13,
            'e': 14,
            'f': 15,
            'g': 16,
            'h': 17,
            'i': 18,
            'j': 19,
            'k': 20,
            'l': 21,
            'm': 22,
            'n': 23,
            'o': 24,
            'p': 25,
            'q': 26,
            'r': 27,
            's': 28,
            't': 29,
            'u': 30,
            'v': 31,
            'w': 32,
            'x': 33,
            'y': 34,
            'z': 35,
            '-': 36,
            '*': 37,
            '!': 38}
with open('images/font.bin', 'rb') as f:
        font = f.read(4992)
def my_text(buf, text, x, y):
    count = 0
    for i in text:
        if i != ' ':
            
            buf.blit(framebuf.FrameBuffer(bytearray(font[font_map[i]*128:(font_map[i]+1)*128]), 8, 8, framebuf.RGB565), x+count*8, y, 48988)
        count += 1