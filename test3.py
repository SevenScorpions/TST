import os
import pandas as pd

# Đường dẫn đến thư mục chứa các tệp
folder_path = 'Data'

# Đọc danh sách tên tệp từ thư mục
file_names = os.listdir(folder_path)

# Đọc dữ liệu từ tệp Excel
excel_data = pd.read_excel('data.xlsx')

# Chuyển cột 'Tên tệp' từ tệp Excel thành một danh sách
excel_file_names = excel_data['File'].tolist()

# Kiểm tra xem tên tệp có trong danh sách tên tệp Excel không
for file_name in file_names:
    if not (file_name in excel_file_names):
        print(f"Tệp '{file_name}' không tồn tại trong 'data.xlsx'")
