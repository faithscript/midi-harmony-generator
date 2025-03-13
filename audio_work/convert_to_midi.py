from mido import MidiFile, MidiTrack, Message
import librosa

# Extracted MIDI notes from previous step
midi_notes = [36, 36, 36, 46.6, 46.8, 46.8]  # Replace with actual extracted notes
midi_notes = [int(round(n)) for n in midi_notes]  # Round and convert to int

# Create a new MIDI file and track
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Add MIDI notes to the track
for note in midi_notes:
    track.append(Message('note_on', note=note, velocity=64, time=0))  # Note on
    track.append(Message('note_off', note=note, velocity=64, time=200))  # Note off

# Save the MIDI file
midi_filename = "extracted_melody.mid"
mid.save(midi_filename)
print(f"Saved MIDI file: {midi_filename}")
