from mido import MidiFile, MidiTrack, Message

# load file from isolated
mid = MidiFile("isolated_track.mid")
melody_track = mid.tracks[0]

new_mid = MidiFile()
new_track = MidiTrack()
new_mid.tracks.append(new_track)

for msg in melody_track:
    new_track.append(msg)  # Keep all original messages

    if msg.type == 'note_on':  # Only add harmony to played notes
        third = msg.note + 4  # Major 3rd interval
        fifth = msg.note + 7  # Perfect 5th interval

        # Add the harmonized notes with the same velocity and timing
        #new_track.append(Message('note_on', note=third, velocity=msg.velocity, time=0))
        new_track.append(Message('note_on', note=fifth, velocity=msg.velocity, time=0))

    elif msg.type == 'note_off':  # Ensure harmonized notes turn off too
        third = msg.note + 4
        fifth = msg.note + 7

        #new_track.append(Message('note_off', note=third, velocity=msg.velocity, time=0))
        new_track.append(Message('note_off', note=fifth, velocity=msg.velocity, time=0))

# Save the new harmonized track
new_mid.save("harmonized_track.mid")
print("Saved as 'harmonized_track.mid' with added 3rd and 5th harmonies")
