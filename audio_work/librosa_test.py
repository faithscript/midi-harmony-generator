import soundfile as sf
import librosa

audio_path = "audio_work/looperman-l-1700729-0391350-glory-polo-g-x-rod-wave-piano.wav"

# Load audio using soundfile instead of librosa.load()
y, sr = sf.read(audio_path)

# Convert to mono if it's stereo
if len(y.shape) > 1:
    y = librosa.to_mono(y.T)

print(f"Loaded {audio_path} with sample rate {sr}")
