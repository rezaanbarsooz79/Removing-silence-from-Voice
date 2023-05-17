from pydub import AudioSegment
from pydub.silence import split_on_silence

# load audio file
audio_file = AudioSegment.from_wav(
    "C:/Users/LENOVO/Desktop/remove nose/3.wav")

# split audio on silence
chunks = split_on_silence(audio_file, min_silence_len=500, silence_thresh=-40)

# combine non-silent chunks
combined_audio = AudioSegment.empty()
for chunk in chunks:
    combined_audio = combined_audio.append(chunk, crossfade=0)

# export output file
combined_audio.export("output.wav", format="wav")
