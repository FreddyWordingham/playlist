import numpy as np
import matplotlib.pyplot as plt


# Plot statistics about a given list.
def run(plist):
    print(f"Plotting statistics...")

    # Collect data.
    tracks = plist['Tracks']
    years = []
    durations = []
    for (id, track) in tracks.items():
        try:
            years.append(track['Year'])
            durations.append(track['Total Time'] // 1000)
        except:
            pass

    # Analyse data.
    if len(years) > 0:
        print(f"Found {len(years)} track data.")
    else:
        print("No track data found!")
        return

    x = np.array(durations, np.int32) / 60
    y = np.array(years,  np.int32)

    plt.subplot(2, 1, 1)
    plt.plot(x, y, 'o')
    plt.xlabel('Track duration (min)')
    plt.ylabel('Track year')

    plt.subplot(2, 1, 2)
    plt.hist(x, bins=100)
    plt.xlabel('Track duration (min)')
    plt.ylabel('Count')

    plt.show()
