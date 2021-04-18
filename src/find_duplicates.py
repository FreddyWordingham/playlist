import re
import argparse
import sys
from matplotlib import pyplot
import plistlib
import numpy as np


# Find the duplicates in a given list.
# Save duplicate entries to the output file.
def run(plist, outfile):
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
    f = open(outfile, "w")
    for (name, count) in dups:
        f.write(f"[{name}] {count}\n")
    f.close()
    print(f"Track names saved to {outfile}")
