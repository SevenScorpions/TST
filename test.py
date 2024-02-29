import os
import re
import pandas as pd
from openpyxl import load_workbook
import shutil

def process_folder(new_data_folder_path,data_folder_path, output_df, audio_type, data_wb):
    audio_prefix = "audio_w" if audio_type == "AUDIO WORD" else "audio_s"

    file_count = len([f for f in os.listdir(data_folder_path)])

    for filename in os.listdir(new_data_folder_path):
        if filename.endswith(".mp3") or filename.endswith(".m4a"):
            file_number = filename.split(".")[0]
            file_number = file_number.split("-")[0]
            new_file_number = int(file_number) + file_count + 20
            new_filename = f"{audio_prefix}{new_file_number}.wav"

            # Read data from words.xlsx and sens.xlsx
            words_df = pd.read_excel(os.path.join('Data Detail', 'AUDIO WORD.xlsx'), header=None)
            sens_df = pd.read_excel(os.path.join('Data Detail', 'DATA Me Hue 29.2.xlsx'), header=None)

            # Get data from respective rows
            if audio_prefix == "audio_s":
                row_2 = sens_df.iloc[int(file_number) - 1, 2]
                row_3 = sens_df.iloc[int(file_number) - 1, 1]
            else:
                row_2 = words_df.iloc[int(file_number) - 1, 2]
                row_3 = words_df.iloc[int(file_number) - 1, 1]

            # Remove "12.", "13.",... at the beginning of row_3
            row_3 = re.sub(r'^\d+\.', '', row_3.strip())

            # Append data to the output DataFrame
            output_df = pd.concat([output_df, pd.DataFrame({"File": [new_filename], "Mnong Transcript": [row_2], "Transcript": [row_3]})])
            new_file_path = os.path.join(data_folder_path, new_filename)
            file_path = os.path.join(new_data_folder_path, filename)

            # Move the file to the 'New Data' folder
            shutil.move(file_path, new_file_path)
            print("moved",file_path,"to",new_file_path)

            # Check if sheet 2 exists, otherwise create it
            if "Sheet1" not in data_wb.sheetnames:
                sheet1 = data_wb.create_sheet(title="Sheet1")
                sheet1.append(["File", "Mnong Transcript", "Transcript"])
            else:
                sheet1 = data_wb["Sheet1"]

            # Add data to sheet 2 of the Excel file
            sheet1.append([new_filename, row_2, row_3])

    return output_df

def main():
    new_data_folder = "New Data"
    data_folder = "Data"
    output_df = pd.DataFrame(columns=["File", "Mnong Transcript", "Transcript"])

    # Load existing Excel workbook
    data_wb_path = "data.xlsx"
    if os.path.exists(data_wb_path):
        data_wb = load_workbook(data_wb_path)
    else:
        data_wb = load_workbook()

    for subfolder in os.listdir(new_data_folder):
        subfolder_path = os.path.join(new_data_folder, subfolder)
        if os.path.isdir(subfolder_path):
            output_df = process_folder(subfolder_path,data_folder, output_df, subfolder, data_wb)

    # Save the result to data.xlsx
    data_wb.save(data_wb_path)

if __name__ == "__main__":
    main()
