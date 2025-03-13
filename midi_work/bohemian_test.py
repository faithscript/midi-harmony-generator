from mido import MidiFile, MidiTrack, MidiFile

mid = MidiFile("bohemian.mid")
new_mid = MidiFile()
new_track = MidiTrack()
new_mid.tracks.append(new_track)

index = 3
for msg in mid.tracks[index]:  # Change this index to test different tracks
    msg.time = int(msg.time * 3.5)
    new_track.append(msg)
    

new_mid.save("isolated_track.mid")
print("Saved as 'isolated_track.mid'")

