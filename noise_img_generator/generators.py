import numpy as np
import random
from perlin import PerlinNoiseFactory
from utils import normalize


def random_noise(size, cluster, imgs, norms):
    # generate random image matrix
    p = [[random.randint(0, 255) for c in range(size)] for r in range(size)]

    # sum multiple random images to create larger groups
    for img in range(imgs - 1):
        if (img + 1) % 5 == 0:
            print('generating image:', img + 1)
        img = [[random.randint(0, 255) for c in range(size)] for r in range(size)]
        for row in range(len(p)):
            for col in range(len(p[row])):
                p[row][col] += img[row][col]

    # avg pixels in clusters to form larger groups
    if cluster:
        if size % cluster != 0:
            raise Exception('Size must be evenly divisable by cluster size!')

        for row in range(0, len(p), cluster):
            for col in range(0, len(p[0]), cluster):
                # compute avg within subset
                sum_value = 0
                for offset in range(cluster):
                    sum_value = sum_value + np.sum(p[row + offset][col:col + cluster])
                avg_value = round(sum_value / (cluster * cluster))

                # update all values to use average
                for row_offset in range(cluster):
                    for col_offset in range(cluster):
                        p[row + row_offset][col + col_offset] = avg_value

    # normalize values to increase range
    for norm in range(norms):
        p = normalize(p, 255)

    return p


def perlin_noise(size, dimensions, octaves, tile):
    pnf = PerlinNoiseFactory(dimensions, octaves, tile)
    p = [[pnf(row / size, col/size) for col in range(size)] for row in range(size)]
    p = normalize(p, 255)
    return p

