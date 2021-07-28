import png

def normalize(p, new_max):
    absolute_max = 0
    absolute_min = 255
    for row in range(len(p)):
        cur_max = max(p[row])
        cur_min = min(p[row])
        if cur_max > absolute_max:
            absolute_max = cur_max
        if cur_min < absolute_min:
            absolute_min = cur_min

    for row in range(len(p)):
        for col in range(len(p[row])):
            p[row][col] = round((p[row][col] - absolute_min) / (absolute_max - absolute_min) * new_max)

    return p

def write_noise(p, size, filename):
    w = png.Writer(size, size, greyscale=True)
    f = open(filename, 'wb')
    w.write(f, p)
    f.close()

