import argparse, shutil, re, os


def testPath(path):
    t_path = path.split('\\')
    tstp = [item for item in t_path if item not in src_lst]
    return tstp


parser = argparse.ArgumentParser(
    description='Moves files and folders to a new location.')
parser.add_argument(
    'pathfrom',
    metavar='PATHFROM',
    nargs=1,
    help='a path where files will be moved from')
parser.add_argument(
    'pathto',
    metavar='PATHTO',
    nargs=1,
    help='a path where files will be moved to')

args = parser.parse_args()
src = args.pathfrom[0]
dest = args.pathto[0]

video_pattern = "(.mp4|.avi|.mkv|.wmv|.flv)$"
season_pattern = '(s[0-9]{1,2}|(season|sería|seria)( )*[0-9]+)'

src_lst = src.split("\\")
dest_lst = dest.split("\\")

for root, dirs, files in os.walk(src):
    for name in files:
        name = str(name)
        path_from = os.path.join(root, name)
        pf_lower = path_from.lower()
        if re.search(video_pattern,
                     pf_lower) and not re.search('sample', pf_lower):
            if re.search(season_pattern, pf_lower):
                #tvshow = findTVname(pf_lower)  # USE THIS
                #season = findSeasonNumber(pf_lower)  # USE THIS
                #dest_test = os.path.join(dest, tvshow, season)  # USE THIS
                tstpth = testPath(path_from)
                dest_test = os.path.join(dest, *tstpth)
                #shutil.move(path_from, dest_test)
                if not os.path.exists(dest_test):
                    os.makedirs(dest_test)
                #print(final_dest)
                #if not os.path.isfile(os.path.join(dest_test, name)):
                #    shutil.copy(path_from, dest_test)
                shutil.move(path_from, dest_test)
                #shutil.move(path_from, dest)