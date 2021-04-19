import find_duplicates
import find_common
import plot_stats


# Load an ITunes plist file.
def load_plist(filename):
    import plistlib
    with open(filename, 'rb') as f:
        plist = plistlib.load(f)
        return plist


find_duplicates.run(load_plist("res/library.xml"), "dups.txt")
find_common.run([
    load_plist("res/library.xml"),
    load_plist("res/run.xml"),
], "common.txt")
plot_stats.run(load_plist("res/library.xml"))
