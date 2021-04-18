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
    print(f"Finding duplicate tracks in {plist}")


filename = "res/library.xml"
plist = load_plist(filename)
find_duplicates(plist)
