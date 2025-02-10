import os
import csv

# Function to find .wav files smaller than the specified size limit
def find_small_wav_files(directory, size_limit_kb):
    small_files = []
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return small_files
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.wav'):
                file_path = os.path.join(root, file)
                if os.path.getsize(file_path) < size_limit_kb * 1024:
                    small_files.append(os.path.splitext(file)[0])  # Add file name without extension
    return small_files

# Function to update the CSV file by removing rows that start with names from the small_files list
def update_csv(csv_path, small_files):
    if not os.path.exists(csv_path):
        print(f"CSV file {csv_path} does not exist.")
        return
    rows_to_keep = []
    with open(csv_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='|')
        for row in reader:
            if not any(row[0].startswith(small_file) for small_file in small_files):
                rows_to_keep.append(row)  # Keep rows that do not start with any name in small_files
            else:
                print(f"Line starting with {row[0]} found in small_files and will be removed.")
    
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerows(rows_to_keep)  # Write the filtered rows back to the CSV file

if __name__ == "__main__":
    wav_directory = "wavs"  # Directory to search for .wav files
    csv_file_path = "metadata.csv"  # Path to the CSV file
    size_limit_kb = 25  # Size limit in kilobytes

    small_wav_files = find_small_wav_files(wav_directory, size_limit_kb)  # Find small .wav files
    update_csv(csv_file_path, small_wav_files)  # Update the CSV file
