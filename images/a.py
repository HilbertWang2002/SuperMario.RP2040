import imageio
import numpy as np
'''
im = imageio.imread('font.png')
for j in range(16):
    for i in range(3):
        imageio.imwrite(f'fonts/{i*16+j}.png', im[i*8:(i+1)*8,j*8:(j+1)*8,:])
'''
imgs = []
for i in range(39):
    imgs.append(imageio.imread(f'fonts/{i}.png'))
imageio.imwrite('fonts/font.png', np.vstack(imgs))
