import os
from pathlib import Path


INPUT_DIR = "input"
OUTPUT_DIR = "output"


# Returns a list of all file paths inside a parent directory recursively, does not return folders
def get_all_files_in_dir(parent_path):
    all_files = []
    for path in os.listdir(parent_path):
        path = os.path.join(parent_path, path)
        path = os.path.abspath(path)
        if os.path.isfile(path):
            all_files.append(path)
        elif os.path.isdir(path):  # This is a directory, so get files inside of it
            all_files += (get_all_files_in_dir(path))  # Recursive add songs inside child dir
    return all_files


def filter_to_mp3(file_paths):
    for path in file_paths:
        pass



a = get_all_files_in_dir(INPUT_DIR)
for b in a:
    print(b)
















