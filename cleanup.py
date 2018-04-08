# filled with regex tests

import os
import re
import shutil
import argparse
import sys

# test
#src = arg1
#dest = arg2

# this code snippet goes through all the files in the folder you are in and prints out it's full path
pattern = "(.mp4|.avi|.mkv|.wmv|.flv)$"
for root, dirs, files in os.walk('.'):
    for name in files:
        name = str(name)
        name = os.path.realpath(os.path.join(root, name))
        #if name.lower().endswith('.mp4', '.avi', '.mkv', '.wmv', '.flv'):
        if re.search(pattern, name):
            print(name)

pattern = "(.mp4|.avi|.mkv|.wmv|.flv)$"
for root, dirs, files in os.walk('.'):
    for name in files:
        name = str(name)
        name = os.path.join(root, name)
        if re.search(pattern, name):
            print(name)

pattern = "(.mp4|.avi|.mkv|.wmv|.flv)$"
for root, dirs, files in os.walk('.'):
    for name in files:
        name = str(name)
        name = os.path.join(root, name)
        if re.search(pattern, name):
            if re.search('(S|s)[0-9]{2}', name.lower()):
                print(name.lower())

#pattern = "(.mp4|.avi|.mkv|.wmv|.flv)$"
#for root, dirs, files in os.walk('.'):
#    for name in files:
#        name = str(name)
#        name = os.path.realpath(os.path.join(root, name))
#        name = name.lower()
#        if re.search(pattern, name):
#            if re.search('s[0-9]{2}', name) or re.search(
#                    'season/\s*[0-9]+', name):
#                print(name)

pattern = "(.mp4|.avi|.mkv|.wmv|.flv)$"
for root, dirs, files in os.walk('.'):
    for name in files:
        name = str(name)
        name = os.path.realpath(os.path.join(root, name))
        name = name.lower()
        if re.search(pattern, name):
            if re.search('season( )*[0-9]+', name):
                print(name)

video_pattern = "(.mp4|.avi|.mkv|.wmv|.flv)$"
for root, dirs, files in os.walk('.'):
    for name in files:
        name = str(name)
        name_path = os.path.realpath(os.path.join(root, name))
        name_lower = name.lower()
        if re.search(video_pattern, name_lower):
            if re.search('s[0-9]{2}', name_lower) or re.search(
                    'season( )*[0-9]+', name_lower):
                test = name_path.split('\\')
                for item in test:
                    if os.path.isfile(item):
                        print(item)

for root, dirs, files in os.walk('.'):
    for directory in dirs:
        directory = str(directory)
        dir_lower = directory.lower()
        if re.search('season', dir_lower):
            path = os.path.realpath(os.path.join(root, directory))
            print(path)

for root, dirs, files in os.walk('.'):
    for directory in dirs:
        directory = str(directory)
        dir_lower = directory.lower()
        if re.search('season', dir_lower):
            path = os.path.join(root, directory)
            print(path)

for root, dirs, files in os.walk('.'):
    for directory, name in dirs, files:
        print(str(directory))

#if not os.path.exists('downloads'):
#    fr, to = sys.argv[1:]
#else:
#    fr = 'downloads'
#    to = 'sorted'

# afrita frekar en að færa

str1 = 's03'
str2 = 's1'
str3 = 'season 1'

season_number = ''.join(
    [str1[i] for i in range(len(str1)) if str1[i].isdigit()])
if 0 < len(season_number) < 2:
    season = 'Season 0' + season_number
else:
    season = 'Season ' + season_number

#and re.search('^(?!sample)', pf_lower)

tvname = []
filename = '8.out.of.10.cats.s03e07.pdtv.xvid-ttt.avi'
fsplit = filename.split('.')
for each in fsplit:
    if re.match('s0', each):
        break
    tvname.append(each)
print(tvname)