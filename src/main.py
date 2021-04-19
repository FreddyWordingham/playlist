import find_duplicates
import find_common
import plot_stats
import argparse


# Load an ITunes plist file.
def load_plist(filename):
    import plistlib
    with open(filename, 'rb') as f:
        plist = plistlib.load(f)
        return plist


# Analyses playlist files exported from iTunes.
def main():
    parser = argparse.ArgumentParser(
        description="Analyse iTunes playlist files.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--common', nargs='*', dest='plFiles', required=False)
    group.add_argument('--stats', dest='plFile', required=False)
    group.add_argument('--dup', dest='plFileD', required=False)

    args = parser.parse_args()
    if args.plFiles:
        lists = []
        for file in args.plFiles:
            lists.append(load_plist(file))
        find_common.run(lists, "common.txt")
    elif args.plFile:
        plot_stats.run(load_plist(args.plFile))
    elif args.plFileD:
        find_duplicates.run(load_plist(args.plFileD), "dups.txt")
    else:
        print("These are not the tracks you are looking for.")


main()
