import imageio
import numpy as np
import os
for k in os.listdir():
    if k.endswith('.py'):
        continue
    im = imageio.imread(k)
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            if im[i][j][3]==0:
                im[i, j, 0:3] = [107, 140, 255]
    imageio.imwrite(k, im)