import os
import matplotlib.pyplot as plt
from pydub.utils import mediainfo

def get_audio_lengths(directory):
    audio_lengths = []
    for filename in os.listdir(directory):
        if filename.endswith('.mp3') or filename.endswith('.wav'):
            filepath = os.path.join(directory, filename)
            info = mediainfo(filepath)
            length = float(info['duration'])# Convert milliseconds to seconds
            audio_lengths.append(length)
    return audio_lengths

def plot_audio_lengths(directory):
    audio_lengths = get_audio_lengths(directory)
    plt.hist(audio_lengths, bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Length (seconds)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Audio Lengths')
    plt.grid(True)
    plt.show()

# Thay 'Data' bằng đường dẫn đến thư mục chứa các file âm thanh của bạn
folder_path = 'Data'
plot_audio_lengths(folder_path)
