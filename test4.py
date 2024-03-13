import os
from pydub.utils import mediainfo

# Đường dẫn tới thư mục chứa các file âm thanh
folder_path = "Data"

# Hàm để tính tổng độ dài của tất cả các file âm thanh trong thư mục
def total_audio_duration(folder_path):
    total_duration = 0

    # Duyệt qua tất cả các file trong thư mục
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            # Kiểm tra nếu file có định dạng âm thanh
            if filename.lower().endswith(('.mp3', '.wav', '.ogg', '.flac')):
                # Sử dụng mediainfo để lấy thông tin về độ dài của file âm thanh
                audio_info = mediainfo(filepath)
                duration = float(audio_info['duration'])
                total_duration += duration

    return total_duration

# Tính tổng độ dài của tất cả các file âm thanh trong thư mục
total_duration = total_audio_duration(folder_path)
print("Tổng độ dài của tất cả các file âm thanh trong thư mục là:", total_duration, "giây")
