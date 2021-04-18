import find_duplicates


# Load an ITunes plist file.
def load_plist(filename):
    import plistlib
    with open(filename, 'rb') as f:
        plist = plistlib.load(f)
        return plist


filename = "res/library.xml"
outfile = "dups.txt"
plist = load_plist(filename)
find_duplicates.run(plist, outfile)
