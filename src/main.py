import re
import argparse
import sys
from matplotlib import pyplot
import plistlib
import numpy as np


def load_plist(filename):
    with open(filename, 'rb') as f:
        plist = plistlib.load(f)
        return plist


def find_duplicates(plist):
    # print(f"Finding duplicate tracks in {plist}")
    tracks = plist['Tracks']
    names = {}
    for (track_id, track) in tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time'] // 1000
            if name in names:
                if duration == names[name][0]:
                    count = names[name][1]
                    names[name] = (duration, count + 1)
            else:
                names[name] = (duration, 1)
        except:
            pass
    for (name, (time, count)) in names.items():
        if count > 1:
            print(f'{name}\t{count}')


filename = 'res/library.xml'
plist = load_plist(filename)
find_duplicates(plist)
