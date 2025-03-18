import os
import wave
import shutil
from pydub import AudioSegment

def list_and_convert_stereo_wav_files(folder_path):
    stereo_files = []
    converted_folder = os.path.join(folder_path, 'Converted_To_MONO')
    os.makedirs(converted_folder, exist_ok=True)
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.wav'):
            file_path = os.path.join(folder_path, filename)
            with wave.open(file_path, 'rb') as wav_file:
                channels = wav_file.getnchannels()
                if channels != 1:
                    stereo_files.append(filename)
                    # Convert to mono
                    audio = AudioSegment.from_wav(file_path)
                    mono_audio = audio.set_channels(1)
                    mono_file_path = os.path.join(converted_folder, filename)
                    mono_audio.export(mono_file_path, format="wav")
    return stereo_files

folder_path = 'wavs'
stereo_files = list_and_convert_stereo_wav_files(folder_path)
print("Stereo (2-channel) .wav files:")
for file in stereo_files:
    print(file)