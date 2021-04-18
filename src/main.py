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
    print(f"Finding duplicate tracks...")

    # Collect data.
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

    # Filter duplicates.
    dups = []
    for (name, (time, count)) in names.items():
        if count > 1:
            dups.append((name, count))

    if len(dups) > 0:
        print(f"Found {len(dups)} duplicates.")
    else:
        print("No duplicate tracks found!")

    # Save data.
    f = open("dups.txt", "w")
    for (name, count) in dups:
        f.write(f"[{name}] {count}\n")
    f.close()
    print(f"Track names saved to dup.txt")


filename = "res/library.xml"
plist = load_plist(filename)
find_duplicates(plist)
