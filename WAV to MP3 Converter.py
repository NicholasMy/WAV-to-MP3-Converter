import os

# User variables here:
INPUT_DIR = "input"
OUTPUT_DIR = "output"

# End of user variables

INPUT_DIR = os.path.abspath(INPUT_DIR)
OUTPUT_DIR = os.path.abspath(OUTPUT_DIR)


# Returns a list of all file paths inside a parent directory recursively, does not return folders
def get_all_files_in_dir(parent_path):
    all_files = []
    for path in os.listdir(parent_path):
        path = os.path.join(parent_path, path)
        if os.path.isfile(path):
            all_files.append(path)
        elif os.path.isdir(path):  # This is a directory, so get files inside of it
            all_files += (get_all_files_in_dir(path))  # Recursive add songs inside child dir
    return all_files


def filter_to_wav(file_paths):
    wav = []
    for path in file_paths:
        name, ext = os.path.splitext(path)
        if ext == ".wav":
            wav.append(path)
    return wav


# Gets the full path to the new mp3 file given a wav file and the output directory where the new file should be saved
def get_new_file_name(old_file_name, output_directory):
    old_file_name_without_drive = os.path.splitdrive(old_file_name)[1]
    old_file_name_without_extension = os.path.splitext(old_file_name_without_drive)[0]
    partial_new_file_name = old_file_name_without_extension + ".mp3"
    new_file_name = output_directory + partial_new_file_name
    return new_file_name


all_files = get_all_files_in_dir(INPUT_DIR)

all_wav = filter_to_wav(all_files)
for i in all_wav[:1]:
    print(get_new_file_name(i, OUTPUT_DIR))














