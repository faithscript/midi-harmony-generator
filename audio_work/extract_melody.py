import librosa
import numpy as np
import soundfile as sf
from mido import Message, MidiFile, MidiTrack

# Load audio file
audio_path = "audio_work/looperman-l-1700729-0391350-glory-polo-g-x-rod-wave-piano.wav"
y, sr = sf.read(audio_path)

# Convert stereo to mono if needed
if len(y.shape) > 1:
    y = librosa.to_mono(y.T)

# Extract pitch using pYIN
f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))

# Convert frequency to MIDI notes (only keep voiced parts)
midi_notes = librosa.hz_to_midi(f0)
midi_notes = midi_notes[~np.isnan(midi_notes)]  # Remove NaNs (unvoiced parts)

# Normalize amplitudes for velocity scaling (convert absolute amplitude to 0-127 MIDI scale)
amplitudes = np.abs(y)  # Get absolute amplitude values
amplitudes = amplitudes[:len(midi_notes)]  # Match length with MIDI notes
velocity = np.interp(amplitudes, (np.min(amplitudes), np.max(amplitudes)), (50, 100))  # Scale to 50-100 MIDI range

# Create MIDI file
midi_file = MidiFile()
track = MidiTrack()
midi_file.tracks.append(track)

# Add notes with velocity variations
for note, vel in zip(midi_notes, velocity):
    midi_note = int(round(note))  # Round to nearest MIDI note
    midi_velocity = int(round(vel))  # Convert velocity to integer
    track.append(Message('note_on', note=midi_note, velocity=midi_velocity, time=0))
    track.append(Message('note_off', note=midi_note, velocity=midi_velocity, time=200))  # Fixed duration for now

# Save MIDI file
midi_output_path = "extracted_melody_dynamic.mid"
midi_file.save(midi_output_path)

print(f"Saved MIDI with dynamic velocity: {midi_output_path}")
