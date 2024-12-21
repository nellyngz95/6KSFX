#Audio Augmentation Chain
import numpy as np
import torchaudio
import torch
import os
import glob
# Add the path to the directory where `audio_augmentations` is located
import sys

from torchaudio_augmentations import *
import matplotlib.pyplot as plt

def apply_transforms(audio, sr, num_samples):
    transforms = [
    RandomApply([Noise(min_snr=0.001, max_snr=0.005)], p=0.3),
    HighLowPass(sample_rate=sr), # this augmentation will always be applied in this aumgentation chain!
    RandomApply([PitchShift(
        n_samples=num_samples,
        sample_rate=sr
    )], p=0.4),
    RandomApply([Reverb(sample_rate=sr)], p=0.3)]
    return transforms

def load_audio(file_path, output_base_path):
    count_wav_files = 0
    trans_wav_files = 0 
    for file in glob.glob(os.path.join(file_path, '**', '*.wav') or os.path.join(file_path,'**','*.mp3'), recursive=True):
        count_wav_files += 1
        audio, sr = torchaudio.load(file)
        transform = Compose(transforms=apply_transforms(audio, sr, audio.size(1)))
        transformed_audio = transform(audio)
        trans_wav_files += 1
        # Generate new file path with 'T' prefix
        rel_path = os.path.relpath(file, file_path)  # Get relative path from base directory
        dir_name, file_name = os.path.split(rel_path)
        new_file_name = 'T' + file_name
        new_dir_path = os.path.join(output_base_path, dir_name)
        
        # Create directories if they don't exist
        os.makedirs(new_dir_path, exist_ok=True)

        new_file_path = os.path.join(new_dir_path, new_file_name)

        # Save transformed audio
        torchaudio.save(new_file_path, transformed_audio, sr)
    print("Original files:", count_wav_files)
    print("Transformed files:", trans_wav_files)
    if count_wav_files > 0:
        print("Sample Rate:", sr, "Audio Size:", audio.size(1))
    else:
        print("No WAV files found.")
    return audio, sr, transformed_audio



if __name__ == '__main__':
    print("Audio Augmentation Chain")
    path_dataset = '/Users/nellygarcia/Downloads/st'
    output_base_path = '/Users/nellygarcia/Downloads/st'
    load_audio(path_dataset,output_base_path)