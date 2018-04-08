import argparse, shutil

parser = argparse.ArgumentParser(
    description='Moves files and folders to a new location.')
parser.add_argument(
    'paths',
    metavar='PATH',
    nargs=2,
    help='a path where files will be moved from and to')

args = parser.parse_args()
src = args.paths[0]
dest = args.paths[1]

shutil.move(src, dest)