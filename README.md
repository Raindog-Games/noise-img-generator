# noise_image_generator
CLI tool to generate noise png file to be used in game design.

## Install
```shell
pip3 install noise_img_generator
```

```shell
usage: noise_img_generator [-h] [--gentype GENTYPE] [--size SIZE] [--filename FILENAME]
              [--seed SEED] [--cluster CLUSTER] [--imgs IMGS] [--norms NORMS]
              [--dims DIMS] [--octaves OCTAVES] [--tile TILE [TILE ...]]

Generate noise png files.

optional arguments:
  -h, --help            show this help message and exit
  --gentype GENTYPE     specify a noise generator to use [random, perlin]
                        (default: random)
  --size SIZE           size of output image (default: 512)
  --filename FILENAME   name of file created (default: noise.png)
  --seed SEED           seed to use for generation (default: None)
  --cluster CLUSTER     width of kernal to average neighbouring pixels
                        (default: 0)
  --imgs IMGS           number of random generated images to combine (default:
                        1)
  --norms NORMS         number of times to normalize image (default: 1)
  --dims DIMS           number of dimensions to use with perlin (default: 2)
  --octaves OCTAVES     number of octaves to use with perlin, recommended max
                        4 (default: 1)
  --tile TILE [TILE ...]
                        connected tilings to be used [space dimensions]
                        (default: [1, 1])
```
