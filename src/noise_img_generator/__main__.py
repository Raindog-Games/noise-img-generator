import argparse
import random
from noise_img_generator.utils import write_noise
from noise_img_generator.generators import random_noise, perlin_noise

def cli():
    parser = argparse.ArgumentParser(
            description='Generate noise png files.',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--gentype', type=str, default='random',
                        help='specify a noise generator to use [random, perlin]')
    parser.add_argument('--size', type=int, default=512,
                        help='size of output image')
    parser.add_argument('--filename', type=str, default='noise.png',
                        help='name of file created')
    parser.add_argument('--seed', type=int, default=None,
                        help='seed to use for generation')
    parser.add_argument('--cluster', type=int, default=0,
                        help='width of kernal to average neighbouring pixels')
    parser.add_argument('--imgs', type=int, default=1,
                        help='number of random generated images to combine')
    parser.add_argument('--norms', type=int, default=1,
                        help='number of times to normalize image')
    parser.add_argument('--dims', type=int, default=2,
                        help='number of dimensions to use with perlin')
    parser.add_argument('--octaves', type=int, default=1,
                        help='number of octaves to use with perlin, recommended max 4')
    parser.add_argument('--tile', nargs='+', type=int, default=[1,1],
                        help='connected tilings to be used [space dimensions]')

    args = parser.parse_args()

    random.seed(args.seed) # set seed if included
    # Implement specified noise generator
    if args.gentype == 'random':
        noise = random_noise(args.size, args.cluster, args.imgs, args.norms)
    elif args.gentype == 'perlin':
        noise = perlin_noise(args.size, args.dims, args.octaves, tuple(args.tile))
    else:
        raise ValueError('Noise generator "{0}" does not exist. Run --help to see supported generators.'.format(args.gentype))

    # Write noise to file
    write_noise(noise, args.size, args.filename)

if __name__ == '__main__':
    cli()
