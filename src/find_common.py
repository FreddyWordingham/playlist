import plistlib


# Find common tracks.
def run(plists, outfile):
    print(f"Finding common tracks...")
    track_name_sets = []

   # Collect data.
    for plist in plists:
        names = set()
        tracks = plist['Tracks']
        for (id, track) in tracks.items():
            try:
                names.add(track['Name'])
            except:
                pass
        track_name_sets.append(names)

    # Find common tracks.
    common_tracks = set.intersection(*track_name_sets)

    # Analyse data.
    if len(common_tracks) > 0:
        print(f"Found {len(common_tracks)} common tracks.")
    else:
        print("No common tracks found!")
        return

    f = open(outfile, "w")
    for name in common_tracks:
        # s = "%s\n" % name
        # f.write(s.encode("UTF-8"))
        # s = "%s\n" % name
        f.write(f"{name}\n")
    f.close()
    print(f"Common track names saved to {outfile}")
