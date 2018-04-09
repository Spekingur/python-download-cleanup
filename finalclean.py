#!/bin/bash
# Download cleanup script
# Authors:
# Hreiðar Ólafur Arnarsson, hreidara14@ru.is
# Maciej Sierzputowski, maciej15@ru.is
#
# Version 1

import argparse, shutil, re, os

### ARGUMENT PARSING ###
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


### FUNCTION DEFINITIONS ###
# Definition parses through filename and tries to find a tv show name
def findTVname(path):
    tvsplit = os.path.normpath(path).split(os.sep)
    tvs = [item for item in tvsplit if item not in src_lst]
    tvlist = tvs[:-1]
    tvfilename = ''.join(tvs[-1])
    final_tvname = tvDirWalk(path, tvlist, tvfilename)
    #tvfnsplit = tvfilename.split('.')
    #tvname = []
    #for each in tvfnsplit:
    #    if re.match('s[0-9]', each):
    #        break
    #    if each:
    #        tvname.append(each)
    #if not tvname:
    #    tvname = ['test']
    #final_tvname = ' '.join(tvname).title()
    return final_tvname


def tvDirWalk(path, tv_list, filename):
    found = 'test'
    tvname = ''
    if not tv_list:
        m = re.search(tv_pattern, filename)
        if m:
            found = m.group(0)
        else:
            found = 'unknown'
    else:
        tvcheck = ''.join(tv_list[:1])
        if re.search(season_pattern, tvcheck):
            m = re.search(tv_pattern, tvcheck)
            if m:
                found = m.group(0)
            else:
                tvDirWalk(path, tv_list[1:], filename)
        else:
            found = tvcheck
    tvname = found.replace("'",
                           "").replace('.', ' ').replace('-', ' ').replace(
                               '_', ' ').replace(',', ' ').strip().title()
    print(found)
    print(tvname)
    return tvname


# This definition delivers a list to seasonDirWalk to receive a possible season number
# Returns: String saying Season (some number)
def findSeasonNumber(path):
    seasonsplit = os.path.normpath(path).split(os.sep)
    templist = [item for item in seasonsplit if item not in src_lst]
    dirlist = templist[:-1]
    filename = templist[-1]
    season_number = seasonDirWalk(path, dirlist, filename)
    return createSeasonNumber(season_number)


def createSeasonNumber(season_number):
    if not season_number:
        season_number = '9000'
    if 0 < len(season_number) < 2:
        season = 'Season 0' + season_number
    else:
        season = 'Season ' + season_number
    return season


# Goes through the list from findSeasonNumber to find which the file might belong to
# Returns: A number
def seasonDirWalk(path, season_list, filename):
    found = ''
    if not season_list:
        m = re.search(season_pattern, filename)
        if m:
            found = m.group(0)
        else:
            return ''
    else:
        seasoncheck = season_list[-1]
        m = re.search(season_pattern, seasoncheck)
        if m:
            found = m.group(0)
            if re.search(season_pattern3, found):
                found = found[:2]
        else:
            seasonDirWalk(path, season_list[:-1], filename)
    return ''.join([found[i] for i in range(len(found)) if found[i].isdigit()])


### PATTERNS ###
video_pattern = '(.mp4|.avi|.mkv|.wmv|.flv|.rm)$'
season_pattern = '(s[0-9]{1,2})|((season|sería|seria)[ .-]*[0-9]{1,2})|([0-9]{1,2}[ ]*.[ ]*(season|sería|seria))|([0-9]+x[0-9]+)'
season_pattern2 = 's[0-9][0-9]|s[0-9]|season [0-9]*[0-9]|season i|[0-9]. season'
season_pattern3 = '[0-9]+x[0-9]+'
tv_pattern = '.*?(?=s[0-9])|.+?(?=season( )*[0-9]+)'

### MAIN CODE ###
# Splitting src and dest for later use
src_lst = os.path.normpath(src).split(os.sep)
dest_lst = os.path.normpath(dest).split(os.sep)

# Going through each file, checking for name and season,
# creating paths and then moving/copying files to correct location
for root, dirs, files in os.walk(src):
    for name in files:
        name = str(name)
        path_from = os.path.join(root, name)
        pf_lower = path_from.lower()
        # Filter out non-video files and files with 'sample' in their name
        # (samples are obviously not full videos)
        if re.search(video_pattern,
                     pf_lower) and not re.search('sample', pf_lower):
            # Only work with those files that match season pattern(s)
            if re.search(season_pattern, pf_lower):
                tvshow = findTVname(pf_lower)
                season = findSeasonNumber(pf_lower)
                path_to = os.path.join(dest, tvshow, season)
                if not os.path.exists(path_to):
                    os.makedirs(path_to)
                file_to = os.path.join(path_to, name)
                if not os.path.isfile(file_to):
                    shutil.copy(path_from, path_to)
                    #shutil.move(path_from, path_to)