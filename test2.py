from pydub import AudioSegment
import os

def convert_to_wav(input_file, output_file):
    sound = AudioSegment.from_file(input_file)
    sound.export(output_file, format="wav")

def batch_convert_to_wav(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for file in os.listdir(input_folder):
        if file.endswith(".wav"):
            continue
        input_file = os.path.join(input_folder, file)
        output_file = os.path.join(output_folder, os.path.splitext(file)[0] + ".wav")
        print(input_file)
        convert_to_wav(input_file, output_file)
        os.remove(input_file)
# Thay đổi đường dẫn đến thư mục chứa file bạn muốn chuyển đổi
input_folder = "Data"
# Thay đổi đường dẫn đến thư mục bạn muốn lưu các file .wav chuyển đổi
output_folder = "Data"

batch_convert_to_wav(input_folder, output_folder)
