import mido

# load the track
mid = mido.MidiFile("isolated_track.mid")

'''
loop through all the tracks and prind the index and the name
'''
for i, track in enumerate(mid.tracks):
    print(f"Track {i}: {track.name}, Messages: {len(track)}")