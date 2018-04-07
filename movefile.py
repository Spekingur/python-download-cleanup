import argparse, shutil, re, os

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

video_pattern = "(.mp4|.avi|.mkv|.wmv|.flv)$"

for root, dirs, files in os.walk(src):
    for name in files:
        name = str(name)
        path_from = os.path.realpath(os.path.join(root, name))
        path_to = os.path.realpath(os.path.join(dest, name))
        pf_lower = path_from.lower()
        if re.search(video_pattern, pf_lower):
            if re.search('s[0-9]{2}', pf_lower) or re.search(
                    'season( )*[0-9]+', pf_lower):
                shutil.move(path_from, path_to)
                #shutil.copytree(path_from, path_to)
