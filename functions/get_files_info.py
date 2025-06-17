import os
from pathlib import Path

def get_files_info(working_directory, directory=None):
    work_dir_path = os.path.abspath(working_directory)
    search_in_dir = os.path.abspath(directory)
    print(search_in_dir.startswith(work_dir_path))

get_files_info("calculator", ".")