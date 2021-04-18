import re
import argparse
import sys
from matplotlib import pyplot
import plistlib
import numpy as np
import find_duplicates


def load_plist(filename):
    with open(filename, 'rb') as f:
        plist = plistlib.load(f)
        return plist


filename = "res/library.xml"
outfile = "dups.txt"
plist = load_plist(filename)
find_duplicates.run(plist, outfile)
