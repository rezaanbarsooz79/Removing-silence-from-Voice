# Removing-silence-from-Voice
#This code is for removing silence in Vis and it is used from the python pydub library
#This code uses the PyDub library to load an audio file and then split it based on silence. 
#The input file is loaded using AudioSegment.from_wav as input. After loading, split_on_silence attempts to find segments of audio that contain silence,
#and separates them. Then, non-silent chunks are combined together, and finally saved as the output file "output.wav" using export.
#To achieve this, minimum silence length (min_silence_len) and silence threshold (silence_thresh) are also given as input parameters to split_on_silence.
#The min_silence_len parameter specifies the minimum length of silence (in milliseconds) required for a segment to be separated,
#and the silence_thresh parameter defines the minimum level of sound considered as silence.
