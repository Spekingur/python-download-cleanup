import argparse, shutil, re, os


def findTVname(path):
    tvsplit = path.split('\\')
    tvs = [item for item in tvsplit if item not in src_lst]
    tvfilename = tvs[-1]
    tvfnsplit = tvfilename.split('.')
    tvname = []
    for each in tvfnsplit:
        if re.match('s[0-9]', each):
            break
        #each = each.replace(' ', '')
        #print(each)
        if each:
            tvname.append(each)
        #print(tvname)
    final_tvname = ' '.join(tvname).title()
    #print(tvsplit)
    #print(tvs)
    #print(tvfnsplit)
    #print(final_tvname)
    return final_tvname


def findSeasonNumber(path):
    seasonsplit = path.split('\\')
    season_s = [item for item in seasonsplit if item not in src_lst]
    season_number = seasonDirWalk(season_s)
    #seasonfilename = season_s[-1]
    #seasondir = season_s[:-1]
    #print(seasonfilename)
    #print(seasondir)
    #m = re.search('s[0-9]{1,2}', seasonfilename)
    #m = re.search(season_pattern, seasonfilename)
    #if m:
    #    found = m.group(0)
    #    season_number = ''.join(
    #        [found[i] for i in range(len(found)) if found[i].isdigit()])
    #print(found)
    #else:
    #    season_number = seasonDirWalk(seasondir)
    #    if not season_number:
    #        season_number = '9000'
    if not season_number:
        season_number = '9000'

    if 0 < len(season_number) < 2:
        season = 'Season 0' + season_number
    else:
        season = 'Season ' + season_number
    #print(seasonsplit)
    #print(season)
    return season


def seasonDirWalk(season_list):
    if not season_list:
        return ''
    else:
        seasoncheck = season_list[-1]
        m = re.search(season_pattern, seasoncheck)
        if m:
            found = m.group(0)
            return ''.join(
                [found[i] for i in range(len(found)) if found[i].isdigit()])
        else:
            seasonDirWalk(season_list[:-1])


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

#if os.path.exists(dest):
#    shutil.rmtree(dest)

video_pattern = "(.mp4|.avi|.mkv|.wmv|.flv)$"
season_pattern = '(s[0-9]{1,2}|(season|sería|seria)( )*[0-9]+)'

#src_lst = []
src_lst = src.split("\\")
dest_lst = dest.split("\\")
#dest_lst = []

#if not os.path.exists(dest):
#    os.makedirs(dest)

countfiles = 0
countvideo = 0
countseason = 0
samplecount = 0

for root, dirs, files in os.walk(src):
    for name in files:
        countfiles += 1
        #print(root.split('\\')[-1:])
        name = str(name)
        path_from = os.path.join(root, name)
        pf_lower = path_from.lower()
        if re.search(video_pattern,
                     pf_lower) and not re.search('sample', pf_lower):
            if re.search('sample', pf_lower):
                samplecount += 1
            countvideo += 1
            #            dest_lst = path_from.split("\\")
            #            print(dest_lst)
            #            dest_lst[0] = dest
            #            print(dest_lst)
            #            path_to = "\\".join(dest_lst)
            #            print(path_to)
            #if re.search('s[0-9]{2}', pf_lower) or re.search(
            #        'season( )*[0-9]+', pf_lower):
            if re.search(season_pattern, pf_lower):
                d_lst = []
                countseason += 1
                tvshow = findTVname(pf_lower)  # USE THIS
                d_lst.append(tvshow)
                season = findSeasonNumber(pf_lower)  # USE THIS
                d_lst.append(season)
                dlst = dest_lst + d_lst
                #print(dest_lst)
                #print(d_lst)
                #print('\\'.join(dlst))
                final_dest = '\\'.join(dlst)
                dest_test = os.path.join(dest, tvshow, season)  # USE THIS
                #print(final_dest)
                #print(dest_test)
                if not os.path.exists(dest_test):
                    os.makedirs(dest_test)
                #print(final_dest)
                if not os.path.isfile(os.path.join(dest_test, name)):
                    #    shutil.copy(path_from, final_dest)
                    shutil.move(path_from, dest_test)
            #                print(path_from)
            #                shutil.move(path_from, dest)
#                shutil.copy(path_from, dest)
#                src_lst = path_from.split("\\")
#shutil.move(path_from, path_to)
#shutil.copytree(path_from, path_to)
#print(path_from)
#print(path_to)
#print(countfiles)
#print(countvideo)
#print(countseason)
#print(samplecount)

#print(dest_lst)

#        path_to = os.path.join(dest, name)
#        if not os.path.exists(path_to):
#            os.makedirs(path_to)
